
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        
        items = []
        for i in range(n):
            items.append((nums[i], i))

        self._merge_sort(items, counts)
        
        return counts

    def _merge_sort(self, items: list[tuple[int, int]], counts: list[int]) -> list[tuple[int, int]]:
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        
        left_half = self._merge_sort(items[:mid], counts)
        right_half = self._merge_sort(items[mid:], counts)
        
        return self._merge(left_half, right_half, counts)

    def _merge(self, left: list[tuple[int, int]], right: list[tuple[int, int]], counts: list[int]) -> list[tuple[int, int]]:
        merged_list = []
        i, j = 0, 0
        
        right_elements_passed = 0 
        
        while i < len(left) and j < len(right):
            val_L, idx_L = left[i]
            val_R, idx_R = right[j]
            
            if val_L > val_R:
                merged_list.append(right[j])
                right_elements_passed += 1
                j += 1
            else:
                counts[idx_L] += right_elements_passed
                merged_list.append(left[i])
                i += 1
        
        while i < len(left):
            val_L, idx_L = left[i]
            counts[idx_L] += right_elements_passed
            merged_list.append(left[i])
            i += 1
            
        while j < len(right):
            merged_list.append(right[j])
            j += 1
            
        return merged_list
