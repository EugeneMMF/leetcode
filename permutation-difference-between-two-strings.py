class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos_s = {c:i for i,c in enumerate(s)}
        total = 0
        for i,c in enumerate(t):
            total += abs(i - pos_s[c])
        return total
