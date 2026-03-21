class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_map = {}
        stack = []
        
        for i in range(len(nums2) - 1, -1, -1):
            current_num = nums2[i]
            
            while stack and stack[-1] <= current_num:
                stack.pop()
            
            if not stack:
                next_greater_map[current_num] = -1
            else:
                next_greater_map[current_num] = stack[-1]
            
            stack.append(current_num)
            
        result = []
        for num in nums1:
            result.append(next_greater_map[num])
            
        return result
