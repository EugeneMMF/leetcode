class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        score = 0
        for x in nums:
            total += x
            if total > 0:
                score += 1
        return score
