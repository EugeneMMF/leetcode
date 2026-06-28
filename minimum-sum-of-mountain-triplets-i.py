class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF
        for j in range(1, n-1):
            left_min = INF
            for i in range(j):
                if nums[i] < nums[j] and nums[i] < left_min:
                    left_min = nums[i]
            right_min = INF
            for k in range(j+1, n):
                if nums[k] < nums[j] and nums[k] < right_min:
                    right_min = nums[k]
            if left_min != INF and right_min != INF:
                ans = min(ans, left_min + nums[j] + right_min)
        return -1 if ans == INF else ans
