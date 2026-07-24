class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        inc_start = [0] * n
        inc_start[-1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1
            else:
                inc_start[i] = 1
        low, high = 1, n // 2
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            found = False
            limit = n - 2 * mid
            for i in range(limit + 1):
                if inc_start[i] >= mid and inc_start[i + mid] >= mid:
                    found = True
                    break
            if found:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
