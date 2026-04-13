class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding
        self.idx = 0
        self.rem = encoding[0] if encoding else 0
    def next(self, n):
        last = -1
        while n > 0 and self.idx < len(self.encoding):
            if self.rem == 0:
                self.idx += 2
                if self.idx < len(self.encoding):
                    self.rem = self.encoding[self.idx]
                continue
            take = n if n < self.rem else self.rem
            self.rem -= take
            n -= take
            last = self.encoding[self.idx + 1]
        return -1 if n > 0 else last
