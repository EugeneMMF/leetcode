import math

class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        n = len(arr1)
        max_overall_diff = 0

        for c1 in [1, -1]:
            for c2 in [1, -1]:
                for c3 in [1, -1]:
                    min_val = math.inf
                    max_val = -math.inf
                    
                    for x in range(n):
                        current_val = c1 * arr1[x] + c2 * arr2[x] + c3 * x
                        min_val = min(min_val, current_val)
                        max_val = max(max_val, current_val)
                    
                    max_overall_diff = max(max_overall_diff, max_val - min_val)
            
        return max_overall_diff

