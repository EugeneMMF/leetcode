class Solution:
    def countVowelStrings(self, n: int) -> int:
        from math import comb
        return comb(n + 4, 4)
