import typing
class Solution:
    def maximumTripletValue(self, nums: typing.List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = nums[i] if nums[i] > prefix_max[i - 1] else prefix_max[i - 1]
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = nums[i] if nums[i] > suffix_max[i + 1] else suffix_max[i + 1]
        best = 0
        for j in range(1, n - 1):
            left = prefix_max[j - 1]
            if left > nums[j]:
                val = (left - nums[j]) * suffix_max[j + 1]
                if val > best:
                    best = val
        return best