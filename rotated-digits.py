class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        invalid_digits = {'3', '4', '7'}
        change_rotating_digits = {'2', '5', '6', '9'}
        
        for x in range(1, n + 1):
            s_x = str(x)
            
            is_valid_rotation = True
            is_different = False
            
            for digit_char in s_x:
                if digit_char in invalid_digits:
                    is_valid_rotation = False
                    break
                
                if digit_char in change_rotating_digits:
                    is_different = True
            
            if is_valid_rotation and is_different:
                count += 1
                
        return count
