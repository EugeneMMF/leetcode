class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        cur = float('inf')
        for c in cost:
            cur = c if c < cur else cur
            ans.append(cur)
        return ans
