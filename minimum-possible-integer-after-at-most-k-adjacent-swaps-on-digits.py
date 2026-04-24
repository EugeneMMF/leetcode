class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        from collections import deque
        pos = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            pos[ord(ch) - 48].append(i)
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, idx, val):
                i = idx + 1
                while i <= self.n:
                    self.bit[i] += val
                    i += i & -i
            def sum(self, idx):
                i = idx + 1
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s
        bit = BIT(n)
        for i in range(n):
            bit.add(i, 1)
        res = []
        for _ in range(n):
            for d in range(10):
                if pos[d]:
                    idx = pos[d][0]
                    swaps = bit.sum(idx) - 1
                    if swaps <= k:
                        k -= swaps
                        bit.add(idx, -1)
                        res.append(chr(d + 48))
                        pos[d].popleft()
                        break
        return ''.join(res)
