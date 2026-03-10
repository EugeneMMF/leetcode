class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        is_left_to_right = True

        while remaining > 1:
            if is_left_to_right or (remaining % 2 == 1):
                head += step
            
            remaining //= 2
            step *= 2
            is_left_to_right = not is_left_to_right
        
        return head
