class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        actual = self.bits[idx] ^ self.flipped
        if actual == 1:
            return
        self.bits[idx] = 1 ^ self.flipped
        self.ones += 1

    def unfix(self, idx: int) -> None:
        actual = self.bits[idx] ^ self.flipped
        if actual == 0:
            return
        self.bits[idx] = 0 ^ self.flipped
        self.ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        res = []
        f = self.flipped
        for b in self.bits:
            res.append('1' if (b ^ f) else '0')
        return ''.join(res)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()