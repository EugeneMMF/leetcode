class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        freq = Counter(tiles)
        self.total = 0
        def backtrack():
            for ch in list(freq.keys()):
                if freq[ch] > 0:
                    freq[ch] -= 1
                    self.total += 1
                    backtrack()
                    freq[ch] += 1
        backtrack()
        return self.total
