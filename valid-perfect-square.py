class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            
            # Use a long type for square to avoid overflow if language specific
            # In Python, integers handle arbitrary size, so it's not strictly necessary
            # but conceptually, we are squaring a potentially large number.
            square = mid * mid 

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else: # square > num
                right = mid - 1
        
        return False
