class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        d = goal - s
        return (abs(d) + limit - 1) // limit
