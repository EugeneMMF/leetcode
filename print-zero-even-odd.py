import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.current_val = 1
        self.state = 0 # 0: zero's turn, 1: odd's turn, 2: even's turn
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.lock:
                self.cond.wait_for(lambda: self.state == 0)
                printNumber(0)
                if self.current_val % 2 == 1:
                    self.state = 1
                else:
                    self.state = 2
                self.cond.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                self.cond.wait_for(lambda: self.state == 2 or self.current_val > self.n)
                if self.current_val > self.n:
                    self.cond.notify_all()
                    break
                printNumber(self.current_val)
                self.current_val += 1
                self.state = 0
                self.cond.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                self.cond.wait_for(lambda: self.state == 1 or self.current_val > self.n)
                if self.current_val > self.n:
                    self.cond.notify_all()
                    break
                printNumber(self.current_val)
                self.current_val += 1
                self.state = 0
                self.cond.notify_all()
