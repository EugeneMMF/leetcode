import functools

class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        n = len(boxes)
        
        @functools.lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            
            # Count consecutive boxes of the same color as boxes[j] ending at j.
            # 'k' represents the number of boxes of color boxes[j] that are already
            # conceptually appended to its right (from previous merges).
            # We first find the actual number of boxes of color boxes[j] that are
            # contiguous and ending at 'j'. Let this be 'count_at_end'.
            # 'current_k' will be 'count_at_end + k'.
            
            # Start with 'current_k' being the 'k' additional boxes.
            # 'p' will be the index of the first box to the left of 'j' that is NOT boxes[j],
            # or 'i-1' if all boxes from 'i' to 'j' are boxes[j].
            current_k = k
            p = j
            while p >= i and boxes[p] == boxes[j]:
                p -= 1
                current_k += 1
            
            # Option 1: Remove the entire block of boxes[j]'s color found (boxes[p+1 ... j])
            # along with the 'current_k' conceptually appended boxes.
            # The score for this operation is (current_k * current_k).
            # The remaining problem is to solve for the segment boxes[i ... p],
            # with no additional boxes to its right.
            max_points = current_k * current_k + dp(i, p, 0)

            # Option 2: Try to merge the block of boxes[j]'s color (boxes[p+1 ... j])
            # with an earlier box of the same color, boxes[m], where m is in [i ... p].
            # If boxes[m] == boxes[j], we remove the intermediate segment boxes[m+1 ... p] first.
            # This segment provides dp(m+1, p, 0) points.
            # After this removal, boxes[m] effectively becomes adjacent to our block of
            # 'current_k' boxes. Thus, the new problem is dp(i, m, current_k).
            for m in range(i, p + 1): 
                if boxes[m] == boxes[j]:
                    current_points = dp(i, m, current_k) + dp(m + 1, p, 0)
                    max_points = max(max_points, current_points)
            
            return max_points
        
        # Initial call: consider the entire array boxes[0...n-1] with 0 additional boxes.
        return dp(0, n - 1, 0)
