from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            m = min(s)
            return s.count(m)
        wfreq = [f(w) for w in words]
        wfreq.sort()
        res = []
        for q in queries:
            qf = f(q)
            idx = bisect.bisect_right(wfreq, qf)
            res.append(len(wfreq) - idx)
        return res
