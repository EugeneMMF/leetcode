class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = -10**18
        count = 0
        for x in nums:
            start = max(x - k, cur + 1)
            if start <= x + k:
                cur = start
                count += 1
        return count