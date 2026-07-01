class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        count = 0
        for val in nums:
            pos += val
            if pos == 0:
                count += 1
        return count
