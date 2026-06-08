class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.mem = [0] * n
        self.id_to_indices = {}

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i <= self.n - size:
            if self.mem[i] == 0:
                j = i + 1
                while j < i + size and self.mem[j] == 0:
                    j += 1
                if j == i + size:
                    for k in range(i, i + size):
                        self.mem[k] = mID
                    self.id_to_indices.setdefault(mID, set()).update(range(i, i + size))
                    return i
                else:
                    i = j + 1
            else:
                i += 1
        return -1

    def freeMemory(self, mID: int) -> int:
        indices = self.id_to_indices.get(mID, set())
        cnt = len(indices)
        for idx in indices:
            self.mem[idx] = 0
        self.id_to_indices[mID] = set()
        return cnt

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)