class Solution:
    def findValidPair(self, s: str) -> str:
        counts = [0] * 10
        for ch in s:
            counts[ord(ch) - 48] += 1
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a == b:
                continue
            if counts[ord(a) - 48] == ord(a) - 48 and counts[ord(b) - 48] == ord(b) - 48:
                return a + b
        return ""
