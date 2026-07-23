
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ''
        for i in range(0, len(s), k):
            substring = s[i:i+k]
            hashed_sum = sum(ord(c) - ord('a') for c in substring)
            hashed_char = chr(ord('a') + (hashed_sum % 26))
            result += hashed_char
        return result


