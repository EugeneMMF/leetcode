class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min = [None] * n
        min_left = 10**9 + 1
        for j in range(n):
            if min_left < nums[j]:
                left_min[j] = min_left
            min_left = min(min_left, nums[j])
        right_min = [None] * n
        min_right = 10**9 + 1
        for j in range(n - 1, -1, -1):
            if min_right < nums[j]:
                right_min[j] = min_right
            min_right = min(min_right, nums[j])
        ans = 10**18
        for j in range(1, n - 1):
            if left_min[j] is not None and right_min[j] is not None:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])
        return ans if ans != 10**18 else -1
