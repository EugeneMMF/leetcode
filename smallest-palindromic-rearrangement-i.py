class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        half = []
        middle = ''
        for i in range(26):
            cnt = freq[i]
            half.append(chr(97 + i) * (cnt // 2))
            if cnt % 2 == 1:
                middle = chr(97 + i)
        first_half = ''.join(half)
        return first_half + middle + first_half[::-1]