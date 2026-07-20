class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1000000007
        req = {e: c for e, c in requirements}
        max_inv = n * (n - 1) // 2
        dp_prev = [0] * (max_inv + 1)
        dp_prev[0] = 1
        for i in range(1, n + 1):
            pref = [0] * (max_inv + 1)
            pref[0] = dp_prev[0]
            for j in range(1, max_inv + 1):
                pref[j] = (pref[j - 1] + dp_prev[j]) % MOD
            dp_cur = [0] * (max_inv + 1)
            for k in range(max_inv + 1):
                low = k - i
                val = pref[k]
                if low >= 0:
                    val = (val - pref[low]) % MOD
                dp_cur[k] = val
            if i - 1 in req:
                cnt = req[i - 1]
                new_dp = [0] * (max_inv + 1)
                if 0 <= cnt <= max_inv:
                    new_dp[cnt] = dp_cur[cnt]
                dp_cur = new_dp
            dp_prev = dp_cur
        return sum(dp_prev) % MOD