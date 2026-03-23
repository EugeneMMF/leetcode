class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        max_length = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                current_length = 0
                current_node = i 

                while not visited[current_node]:
                    visited[current_node] = True
                    current_length += 1
                    current_node = nums[current_node]
                
                max_length = max(max_length, current_length)
        
        return max_length
