class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 100000
        cnt = [0] * (MAXV + 2)
        total = [0] * (MAXV + 2)
        ans = 0
        for x in nums:
            c1 = cnt[x - 1] if x - 1 >= 0 else 0
            c2 = cnt[x + 1] if x + 1 <= MAXV else 0
            s1 = total[x - 1] if x - 1 >= 0 else 0
            s2 = total[x + 1] if x + 1 <= MAXV else 0
            newCnt = (1 + c1 + c2) % MOD
            newSum = (x + (s1 + c1 * x) % MOD + (s2 + c2 * x) % MOD) % MOD
            ans = (ans + newSum) % MOD
            cnt[x] = (cnt[x] + newCnt) % MOD
            total[x] = (total[x] + newSum) % MOD
        return ans
