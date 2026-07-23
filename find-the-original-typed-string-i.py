class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        i = 0
        n = len(word)
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            total += length - 1
            i = j
        return total
