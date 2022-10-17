from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time
import traceback, sys


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            
            result = self.fn(*self.args, **self.kwargs)
        except:
            
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            
            self.signals.finished.emit()  # Done



class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #counter
        self.counter = 0

        #gui components
        layout = QVBoxLayout()
        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b2 = QPushButton("SAFE!")
        layout.addWidget(self.l)
        b.pressed.connect(self.oh_no)
        b2.pressed.connect(self.oh_yes)
        layout.addWidget(b)
        layout.addWidget(b2)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()        

        #Timer runs in the background
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        #gui connects



        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    #Functions Set 1
    def progress_fn(self, n):
        print("A")
        print("%d%% done" % n)
        print("A")

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(3)
            progress_callback.emit(n*100/4)

        return "Done Function Set 1."

    def print_output(self, s):
        print("B")
        print(s)
        print("B")

    def thread_complete(self):
        print("C")
        print("THREAD COMPLETE!")
        print("C")

    #Functions Set 2
    def execute_this_fn2(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n*100/4)

        return "Done Function Set 2."
    def progress_fn2(self, n):
        print("X")
        print("%d%% done" % n)
        print("X")


    def print_output2(self, s):
        print("Y")
        print(s)
        print("Y")

    def thread_complete2(self):
        print("Z")
        print("THREAD COMPLETE!")
        print("Z")


        #Pass to connect function
    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
        #worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)
    def oh_yes(self):
        # Pass the function to execute
        worker2 = Worker(self.execute_this_fn2) # Any other args, kwargs are passed to the run function
        #worker2.signals.result.connect(self.print_output2)
        worker2.signals.progress.connect(self.progress_fn2)
        worker2.signals.finished.connect(self.thread_complete2)
        

        # Execute
        self.threadpool.start(worker2)

    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec()