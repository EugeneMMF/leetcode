class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mapping = {}
        for old, new in mappings:
            mapping.setdefault(old, set()).add(new)
        n, m = len(s), len(sub)
        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                c1, c2 = sub[j], s[i + j]
                if c1 == c2:
                    continue
                if c1 in mapping and c2 in mapping[c1]:
                    continue
                ok = False
                break
            if ok:
                return True
        return False
