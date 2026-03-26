class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        # dp[i][j] stores the minimum turns to print substring s[i...j]
        # Initialize dp table. dp[i][j] for i > j will implicitly be 0 due to ranges.
        # Max value for dp[i][j] is j - i + 1 (printing each character individually).
        dp = [[0] * n for _ in range(n)]

        # Base case: a single character substring takes 1 turn
        for i in range(n):
            dp[i][i] = 1

        # Fill the dp table for lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Option 1: Print s[i] by itself in one turn.
                # Then, recursively solve for the remaining substring s[i+1...j].
                # This contributes 1 (for s[i]) + dp[i+1][j] turns.
                # dp[i+1][j] handles the case where i+1 > j (empty string) as 0.
                dp[i][j] = 1 + dp[i+1][j] if i + 1 <= j else 1
                
                # Option 2: Find a character s[k] (where k > i) that is the same as s[i].
                # If s[i] == s[k], we can print s[i] and s[k] in the same turn.
                # This turn effectively prints s[i] (the character) from index i to k.
                # After this turn, s[i] and s[k] are correctly printed.
                # We then need to solve two subproblems:
                # 1. The characters between i and k (s[i+1...k-1]). This costs dp[i+1][k-1] turns.
                #    If i+1 > k-1 (i.e., k = i+1), this is an empty string, costing 0 turns.
                # 2. The characters from k to j (s[k...j]). Since s[k] is already covered by the
                #    s[i] print, the subproblem s[k...j] effectively starts with s[k] already "done".
                #    In this DP formulation, dp[k][j] implicitly handles this by comparing various ways
                #    to print s[k...j], one of which would be to not use a new turn for s[k] if it matches.
                #    Therefore, the cost for this part is dp[k][j].
                
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        # Turns needed for the segment s[i+1...k-1]
                        turns_between = dp[i+1][k-1] if i + 1 <= k - 1 else 0
                        
                        # Turns needed for the segment s[k...j]
                        turns_right = dp[k][j]

                        dp[i][j] = min(dp[i][j], turns_between + turns_right)
        
        return dp[0][n-1]

