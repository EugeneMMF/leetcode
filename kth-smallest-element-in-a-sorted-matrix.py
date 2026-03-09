class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Helper function to count elements less than or equal to a given target
        def count_less_equal(target):
            count = 0
            j = n - 1  # Start from the rightmost column
            for i in range(n):  # Iterate through rows
                # Move left in the current row until matrix[i][j] is less than or equal to target
                while j >= 0 and matrix[i][j] > target:
                    j -= 1
                # All elements from matrix[i][0] to matrix[i][j] are less than or equal to target
                # (j + 1) represents the count of such elements in the current row
                count += (j + 1)
            return count

        # Binary search for the answer (the kth smallest value)
        # The range of possible answers is from the smallest element to the largest element in the matrix
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        
        # 'ans' will store the smallest 'mid' for which count_less_equal(mid) >= k
        ans = high 

        while low <= high:
            mid = low + (high - low) // 2
            
            # If there are k or more elements less than or equal to 'mid',
            # 'mid' could be our answer. We try to find a smaller value.
            if count_less_equal(mid) >= k:
                ans = mid
                high = mid - 1
            # If there are fewer than k elements less than or equal to 'mid',
            # 'mid' is too small. We need to look for a larger value.
            else:
                low = mid + 1
        
        return ans
