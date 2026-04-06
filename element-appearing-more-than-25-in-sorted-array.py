from bisect import bisect_left, bisect_right

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        threshold_count = n // 4

        candidates = [arr[i] for i in [0, n // 4, n // 2, (3 * n) // 4]]

        for candidate in candidates:
            left_idx = bisect_left(arr, candidate)
            right_idx = bisect_right(arr, candidate)
            
            current_count = right_idx - left_idx
            
            if current_count > threshold_count:
                return candidate
        
        return -1
