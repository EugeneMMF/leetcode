class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        max_dist = 0
        
        min_val_so_far = arrays[0][0]
        max_val_so_far = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            current_array_min = arrays[i][0]
            current_array_max = arrays[i][-1]
            
            max_dist = max(max_dist, 
                           abs(current_array_max - min_val_so_far),
                           abs(max_val_so_far - current_array_min))
            
            min_val_so_far = min(min_val_so_far, current_array_min)
            max_val_so_far = max(max_val_so_far, current_array_max)
            
        return max_dist
