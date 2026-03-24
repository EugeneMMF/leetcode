import collections

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        max_len = 0

        for num in counts:
            if (num + 1) in counts:
                current_len = counts[num] + counts[num + 1]
                max_len = max(max_len, current_len)
        
        return max_len
