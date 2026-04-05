import collections

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counts = collections.Counter(arr1)
        
        result = []
        
        for x in arr2:
            result.extend([x] * counts[x])
            counts[x] = 0
            
        remaining_elements_sorted = []
        for num in range(1001): 
            if counts[num] > 0:
                remaining_elements_sorted.extend([num] * counts[num])
        
        result.extend(remaining_elements_sorted)
        
        return result
