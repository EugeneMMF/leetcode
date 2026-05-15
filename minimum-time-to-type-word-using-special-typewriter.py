class Solution:
    def minTimeToType(self, word: str) -> int:
        current = 0
        total = 0
        for ch in word:
            target = ord(ch) - 97
            diff = abs(target - current)
            steps = diff if diff <= 13 else 26 - diff
            total += steps + 1
            current = target
        return total
