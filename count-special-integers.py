class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        L = len(s)
        def perm(a, b):
            res = 1
            for i in range(b):
                res *= a - i
            return res
        count = 0
        for l in range(1, L):
            count += 9 * perm(9, l - 1)
        used = set()
        for i, ch in enumerate(s):
            cur = int(ch)
            for d in range(0, cur):
                if i == 0 and d == 0:
                    continue
                if d in used:
                    continue
                remaining_digits = 10 - (i + 1)
                remaining_positions = L - i - 1
                count += perm(remaining_digits, remaining_positions)
            if cur in used:
                return count
            used.add(cur)
        return count + 1