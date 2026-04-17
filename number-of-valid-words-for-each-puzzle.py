class Solution:
    def findNumOfValidWords(self, words, puzzles):
        freq = {}
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            if bin(mask).count('1') <= 7:
                freq[mask] = freq.get(mask, 0) + 1
        ans = []
        for p in puzzles:
            first = 1 << (ord(p[0]) - 97)
            mask = 0
            for ch in p:
                mask |= 1 << (ord(ch) - 97)
            sub = mask
            total = 0
            while sub:
                if sub & first:
                    total += freq.get(sub, 0)
                sub = (sub - 1) & mask
            ans.append(total)
        return ans
