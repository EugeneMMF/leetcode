class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        ans = 0
        for i, val in enumerate(tickets):
            if i <= k:
                ans += min(val, t)
            else:
                ans += min(val, t - 1)
        return ans
