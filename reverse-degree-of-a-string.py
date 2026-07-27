class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            total += (123 - ord(ch)) * i
        return total
