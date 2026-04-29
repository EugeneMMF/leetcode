class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        remaining = k - n
        i = n - 1
        while remaining > 0 and i >= 0:
            add = 25 if remaining >= 25 else remaining
            res[i] = chr(ord('a') + add)
            remaining -= add
            i -= 1
        return ''.join(res)
