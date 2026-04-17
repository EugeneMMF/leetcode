import threading
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and not (self.current % 3 == 0 and self.current % 5 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    break
                printFizz()
                self.current += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and not (self.current % 5 == 0 and self.current % 3 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    break
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and not (self.current % 15 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    break
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and not (self.current % 3 != 0 and self.current % 5 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    break
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
