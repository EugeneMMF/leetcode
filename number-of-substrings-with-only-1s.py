class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        cnt = 0
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                ans = (ans + cnt * (cnt + 1) // 2) % MOD
                cnt = 0
        ans = (ans + cnt * (cnt + 1) // 2) % MOD
        return ans
