class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(sub, start):
            if not sub:
                return ""
            bad = set()
            for i, ch in enumerate(sub):
                if ch.islower():
                    if ch.upper() not in sub:
                        bad.add(i)
                else:
                    if ch.lower() not in sub:
                        bad.add(i)
            if not bad:
                return sub
            best = ""
            best_start = len(s)
            i = 0
            while i < len(sub):
                if i in bad:
                    i += 1
                    continue
                j = i
                while j < len(sub) and j not in bad:
                    j += 1
                seg_start = start + i
                seg = helper(sub[i:j], seg_start)
                if len(seg) > len(best) or (len(seg) == len(best) and seg_start < best_start):
                    best = seg
                    best_start = seg_start
                i = j
            return best
        return helper(s, 0)