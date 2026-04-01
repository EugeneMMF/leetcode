class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        max_len = 0
        i = 0

        while i < n - 1:
            # Find the start of an increasing sequence
            while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1

            peak_start = i

            # Find the peak of the mountain
            while i < n - 1 and arr[i] < arr[i + 1]:
                i += 1

            peak = i

            # Find the end of the decreasing sequence
            while i < n - 1 and arr[i] > arr[i + 1]:
                i += 1

            mountain_end = i

            # Check if a valid mountain was found
            if peak_start < peak < mountain_end:
                current_len = mountain_end - peak_start + 1
                max_len = max(max_len, current_len)
            
            # If we didn't move, advance i to avoid infinite loop if no increasing sequence is found
            if peak == peak_start:
                i += 1

        return max_len
