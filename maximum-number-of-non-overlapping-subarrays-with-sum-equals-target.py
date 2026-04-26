class Solution:
    def maxNonOverlapping(self, nums, target):
        s = 0
        seen = {0}
        count = 0
        for x in nums:
            s += x
            if s - target in seen:
                count += 1
                s = 0
                seen = {0}
            else:
                seen.add(s)
        return count
