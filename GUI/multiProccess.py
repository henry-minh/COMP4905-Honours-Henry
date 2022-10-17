import multiprocessing
import logging
import time
def worker():
    """worker function"""
    logging.info ('Worker')
    return

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker())
        jobs.append(p)
        p.start()