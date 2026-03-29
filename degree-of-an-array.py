class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        num_info = {}
        
        for i, num in enumerate(nums):
            if num not in num_info:
                num_info[num] = [1, i, i]
            else:
                num_info[num][0] += 1
                num_info[num][2] = i
        
        max_degree = 0
        for info in num_info.values():
            max_degree = max(max_degree, info[0])
            
        min_length = float('inf')
        
        for num_value, info_list in num_info.items():
            current_degree = info_list[0]
            if current_degree == max_degree:
                first_idx = info_list[1]
                last_idx = info_list[2]
                current_length = last_idx - first_idx + 1
                min_length = min(min_length, current_length)
                
        return min_length
