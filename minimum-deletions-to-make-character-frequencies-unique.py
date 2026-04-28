class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s).values()
        used = set()
        deletions = 0
        for f in sorted(freq, reverse=True):
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            used.add(f)
        return deletions
