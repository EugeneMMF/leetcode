class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char_list = list(s)
        n = len(char_list)
        i = 0

        while i < n:
            left = i
            right = min(i + k, n) - 1

            while left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            
            i += 2 * k
        
        return "".join(char_list)
