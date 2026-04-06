class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        # The maximum column index to consider for our DP table.
        # We start at index 0 and want to end at index 0.
        # To reach index `j` from index 0, it takes at least `j` steps (all right moves).
        # To return to index 0 from index `j`, it takes at least `j` steps (all left moves).
        # So, if we are at index `j` after `s` steps, we have `steps - s` steps remaining.
        # We must have `steps - s >= j` to be able to return to 0.
        # This implies `j <= steps - s`. The maximum `j` is when `s` is small (i.e., s=0).
        # When `s=0`, `j <= steps`. So, `j` can't exceed `steps`.
        # Also, `j` cannot exceed `arrLen - 1` because the pointer must stay within array bounds.
        # Therefore, the maximum relevant position in the array is `min(arrLen - 1, steps)`.
        # We only need to compute DP states up to this index.
        
        max_reach_idx = min(arrLen - 1, steps)
        
        # dp[j] will store the number of ways to be at index `j` after a certain number of steps.
        # We use a 1D DP array to optimize space, as the current state only depends on the previous state.
        dp = [0] * (max_reach_idx + 1)
        dp[0] = 1 # After 0 steps, there is 1 way to be at index 0.

        # Iterate for each step from 1 to `steps`
        for _ in range(1, steps + 1):
            new_dp = [0] * (max_reach_idx + 1)
            # Iterate through each possible position `j`
            for j in range(max_reach_idx + 1):
                # Option 1: Ways to reach position `j` by staying at `j` from the previous step
                new_dp[j] = (new_dp[j] + dp[j]) % MOD
                
                # Option 2: Ways to reach position `j` by moving left from `j + 1` at the previous step
                if j + 1 <= max_reach_idx:
                    new_dp[j] = (new_dp[j] + dp[j + 1]) % MOD
                
                # Option 3: Ways to reach position `j` by moving right from `j - 1` at the previous step
                if j - 1 >= 0:
                    new_dp[j] = (new_dp[j] + dp[j - 1]) % MOD
            
            dp = new_dp
        
        return dp[0]

