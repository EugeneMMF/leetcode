class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for ch in word1:
            freq1[ord(ch) - 97] += 1
        for ch in word2:
            freq2[ord(ch) - 97] += 1
        if set(word1) != set(word2):
            return False
        if sorted([c for c in freq1 if c]) != sorted([c for c in freq2 if c]):
            return False
        return True
