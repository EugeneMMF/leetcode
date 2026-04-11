from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(t):
            res = []
            i = 0
            n = len(t)
            while i < n:
                j = i
                while j < n and t[j] == t[i]:
                    j += 1
                res.append((t[i], j - i))
                i = j
            return res
        sg = groups(s)
        ans = 0
        for w in words:
            wg = groups(w)
            if len(sg) != len(wg):
                continue
            ok = True
            for (cs, csz), (cw, cz) in zip(sg, wg):
                if cs != cw:
                    ok = False
                    break
                if csz < 3:
                    if csz != cz:
                        ok = False
                        break
                else:
                    if cz > csz or cz < 1:
                        ok = False
                        break
            if ok:
                ans += 1
        return ans
