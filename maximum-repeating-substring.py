class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while True:
            k += 1
            if word * k not in sequence:
                return k - 1
