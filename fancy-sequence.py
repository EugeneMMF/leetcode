class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.cur_mul = 1
        self.cur_add = 0
        self.base = []

    def append(self, val: int) -> None:
        inv = pow(self.cur_mul, self.MOD - 2, self.MOD)
        adjusted = (val - self.cur_add) % self.MOD
        adjusted = adjusted * inv % self.MOD
        self.base.append(adjusted)

    def addAll(self, inc: int) -> None:
        self.cur_add = (self.cur_add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.cur_mul = self.cur_mul * m % self.MOD
        self.cur_add = self.cur_add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.base):
            return -1
        return (self.base[idx] * self.cur_mul + self.cur_add) % self.MOD

