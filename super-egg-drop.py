class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[e] represents the maximum number of floors that can be determined
        # with 'e' eggs and the current number of moves.
        # We initialize it for 0 moves, so dp[e] is 0 for all e.
        prev_dp = [0] * (k + 1)
        
        # 'm' represents the number of moves.
        # We iterate 'm' starting from 1. In the worst case (1 egg), we might need 'n' moves.
        for m in range(1, n + 1):
            # current_dp will store the max floors for 'm' moves.
            current_dp = [0] * (k + 1)
            
            # 'e' represents the number of eggs.
            for e in range(1, k + 1):
                # The recurrence relation for dp[m][e] is:
                # dp[m][e] = dp[m-1][e-1] (if egg breaks)
                #            + dp[m-1][e]   (if egg doesn't break)
                #            + 1            (for the current floor dropped from)
                #
                # In our space-optimized approach:
                # prev_dp[e-1] corresponds to dp[m-1][e-1]
                # prev_dp[e]   corresponds to dp[m-1][e]
                current_dp[e] = prev_dp[e-1] + prev_dp[e] + 1
                
                # If with 'm' moves and 'e' eggs, we can determine 'n' or more floors,
                # then 'm' is the minimum number of moves.
                if current_dp[e] >= n:
                    return m
            
            # After calculating for the current 'm', update prev_dp for the next iteration.
            prev_dp = current_dp
        
        # This part should theoretically not be reached if n >= 1, 
        # as the loop will always find a solution.
        # If n=0, the problem implies 0 moves, but constraints say n>=1.
        return n
