class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        count = 0
        current_sum = 0
        sorted_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            sorted_sum += sorted_arr[i]
            if current_sum == sorted_sum:
                count += 1
        return count
