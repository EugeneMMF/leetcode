class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        prev = -1
        for x in nums:
            if x == prev:
                curr = 1
            else:
                curr += 1
            total += curr
            prev = x
        return total