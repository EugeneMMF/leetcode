class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
        
        return ans
