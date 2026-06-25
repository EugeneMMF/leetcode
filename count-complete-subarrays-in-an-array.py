import typing

class Solution:
    def countCompleteSubarrays(self, nums: typing.List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        ans = 0
        for i in range(n):
            freq = {}
            distinct = 0
            for j in range(i, n):
                val = nums[j]
                if freq.get(val, 0) == 0:
                    distinct += 1
                freq[val] = freq.get(val, 0) + 1
                if distinct == total_distinct:
                    ans += 1
        return ans
