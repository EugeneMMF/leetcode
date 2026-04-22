class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [None] * (target + 1)
        dp[0] = ""
        for i in range(1, target + 1):
            best = None
            for d in range(9, 0, -1):
                c = cost[d - 1]
                if i >= c and dp[i - c] is not None:
                    cand = dp[i - c] + str(d)
                    if best is None or len(cand) > len(best) or (len(cand) == len(best) and cand > best):
                        best = cand
            dp[i] = best
        return dp[target] if dp[target] is not None else "0"
