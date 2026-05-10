class Solution:
    def replaceDigits(self, s: str) -> str:
        res = list(s)
        for i in range(1, len(s), 2):
            res[i] = chr(ord(res[i-1]) + int(s[i]))
        return ''.join(res)
