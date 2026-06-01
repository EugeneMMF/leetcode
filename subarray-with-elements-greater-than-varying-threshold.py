class Solution:
    def validSubarraySize(self, nums, threshold):
        n = len(nums)
        L = [0] * n
        R = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)
        for i in range(n):
            seg_len = R[i] - L[i] - 1
            min_required = threshold // nums[i] + 1
            if min_required <= seg_len:
                return min_required
        return -1