from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import time

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic1(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        #self._state = randrange(0, 10)
        self._state = 1
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

    def some_business_logic2(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        #self._state = randrange(0, 10)
        self._state = 2
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 1:
            print("ConcreteObserverA: Reacted to the event")

            

        #if subject._state == 2:
        #    print()


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 2:
            print("ConcreteObserverB: Reacted to the event Begin Looping until state set to 1")
            #time.sleep(5)
            while subject._state == 2:

                print("Looping")
                if subject._state == 1:
                    break
        print("Exited Looping stage in observer b, state 2 changed to state 1")

def observerTestBtn(self):
    # The client code.

    self.subject = ConcreteSubject()

    self.observer_a = ConcreteObserverA()
    self.subject.attach(self.observer_a)

    self.observer_b = ConcreteObserverB()
    self.subject.attach(self.observer_b)

    self.subject.some_business_logic1()
    self.subject.some_business_logic1()

    #self.subject.detach(self.observer_a)

    self.subject.some_business_logic1()
    print("///////////////////////////////////////////")

def observerInfoTestBtn(self):
    self.subject.some_business_logic1()
    print("///////////////////////////////////////////")

def observerHelpTestBtn(self):
    self.subject.some_business_logic2()
    print("///////////////////////////////////////////")