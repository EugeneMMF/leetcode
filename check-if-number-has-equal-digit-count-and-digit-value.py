class Solution:
    def digitCount(self, num: str) -> bool:
        counts = [0] * 10
        for ch in num:
            counts[int(ch)] += 1
        for i, ch in enumerate(num):
            if counts[i] != int(ch):
                return False
        return True