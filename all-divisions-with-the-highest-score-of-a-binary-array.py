class Solution:
    def maxScoreIndices(self, nums):
        n = len(nums)
        total_ones = sum(nums)
        zeros_left = 0
        ones_left = 0
        max_score = -1
        indices = []
        for i in range(n + 1):
            score = zeros_left + (total_ones - ones_left)
            if score > max_score:
                max_score = score
                indices = [i]
            elif score == max_score:
                indices.append(i)
            if i < n:
                if nums[i] == 0:
                    zeros_left += 1
                else:
                    ones_left += 1
        return indices