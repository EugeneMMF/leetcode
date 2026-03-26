class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(left_ptr, right_ptr):
            while left_ptr < right_ptr:
                if s[left_ptr] != s[right_ptr]:
                    return False
                left_ptr += 1
                right_ptr -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)
            
            left += 1
            right -= 1
        
        return True
