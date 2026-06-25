class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s1, s2):
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2
            max_overlap = 0
            min_len = min(len(s1), len(s2))
            for k in range(min_len, 0, -1):
                if s1[-k:] == s2[:k]:
                    max_overlap = k
                    break
            return s1 + s2[max_overlap:]
        strings = [a, b, c]
        best = None
        import itertools
        for perm in itertools.permutations(strings):
            merged = merge(perm[0], perm[1])
            merged = merge(merged, perm[2])
            if best is None or len(merged) < len(best) or (len(merged) == len(best) and merged < best):
                best = merged
        return best