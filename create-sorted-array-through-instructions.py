class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        max_val = max(instructions) + 2
        bit = [0] * (max_val)

        def update(i):
            while i < max_val:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        total = 0
        for idx, val in enumerate(instructions, 1):
            less = query(val - 1)
            greater = (idx - 1) - query(val)
            total += less if less < greater else greater
            if total >= MOD:
                total %= MOD
            update(val)
        return total % MOD
