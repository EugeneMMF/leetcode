class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = {c: n for c in set(s)}
        last = {c: -1 for c in set(s)}
        for i, ch in enumerate(s):
            if i < first[ch]:
                first[ch] = i
            if i > last[ch]:
                last[ch] = i
        intervals = []
        seen = set()
        for ch in set(s):
            l, r = first[ch], last[ch]
            expand = True
            while expand:
                expand = False
                for k in range(l, r + 1):
                    c2 = s[k]
                    if first[c2] < l:
                        l = first[c2]
                        expand = True
                    if last[c2] > r:
                        r = last[c2]
                        expand = True
            if (l, r) not in seen:
                seen.add((l, r))
                intervals.append((r, l))
        intervals.sort()
        res = []
        prev = -1
        for r, l in intervals:
            if l > prev:
                res.append(s[l:r + 1])
                prev = r
        return res
