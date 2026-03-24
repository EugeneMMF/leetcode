class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        list2_map = {s: i for i, s in enumerate(list2)}
        
        min_index_sum = float('inf')
        result = []
        
        for i, s1 in enumerate(list1):
            if s1 in list2_map:
                j = list2_map[s1]
                current_sum = i + j
                
                if current_sum < min_index_sum:
                    min_index_sum = current_sum
                    result = [s1]
                elif current_sum == min_index_sum:
                    result.append(s1)
                    
        return result
