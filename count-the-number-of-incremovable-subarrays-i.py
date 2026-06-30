class Solution:
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        prefix_inc = [True] * n
        for i in range(1, n):
            prefix_inc[i] = prefix_inc[i-1] and nums[i-1] < nums[i]
        suffix_inc = [True] * n
        for i in range(n-2, -1, -1):
            suffix_inc[i] = suffix_inc[i+1] and nums[i] < nums[i+1]
        count = 0
        for l in range(n):
            for r in range(l, n):
                left_ok = True if l == 0 else prefix_inc[l-1]
                right_ok = True if r == n-1 else suffix_inc[r+1]
                boundary_ok = True if l == 0 or r == n-1 else nums[l-1] < nums[r+1]
                if left_ok and right_ok and boundary_ok:
                    count += 1
        return count