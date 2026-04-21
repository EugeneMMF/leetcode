class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        def steps(n):
            if n in memo:
                return memo[n]
            if n % 2 == 0:
                res = 1 + steps(n // 2)
            else:
                res = 1 + steps(3 * n + 1)
            memo[n] = res
            return res
        arr = [(steps(i), i) for i in range(lo, hi + 1)]
        arr.sort()
        return arr[k - 1][1]
