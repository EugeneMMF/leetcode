from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0]*n
        right_max = [0]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            left_max[i] = i - stack[-1] if stack else i+1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            right_max[i] = stack[-1] - i if stack else n-i
            stack.append(i)
        sum_max = 0
        for i in range(n):
            sum_max += nums[i]*left_max[i]*right_max[i]
        left_min = [0]*n
        right_min = [0]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left_min[i] = i - stack[-1] if stack else i+1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            right_min[i] = stack[-1] - i if stack else n-i
            stack.append(i)
        sum_min = 0
        for i in range(n):
            sum_min += nums[i]*left_min[i]*right_min[i]
        return sum_max - sum_min
