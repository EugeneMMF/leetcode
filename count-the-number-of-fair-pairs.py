class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n) - 1
            if right >= left:
                ans += right - left + 1
        return ans
