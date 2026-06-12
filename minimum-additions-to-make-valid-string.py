class Solution:
    def addMinimum(self, word: str) -> int:
        pos = 0
        for ch in word:
            desired = 0 if ch == 'a' else 1 if ch == 'b' else 2
            shift = (desired - pos % 3 + 3) % 3
            pos += shift + 1
        L = ((pos + 2) // 3) * 3
        return L - len(word)
