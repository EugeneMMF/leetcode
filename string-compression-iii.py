class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        n = len(word)
        while i < n:
            c = word[i]
            j = i
            while j < n and word[j] == c and j - i < 9:
                j += 1
            comp.append(str(j - i))
            comp.append(c)
            i = j
        return ''.join(comp)
