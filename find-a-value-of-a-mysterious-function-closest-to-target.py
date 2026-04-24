class Solution:
    def closestToTarget(self, arr, target):
        best = 10**9
        cur = set()
        for a in arr:
            nxt = {a}
            for v in cur:
                nxt.add(v & a)
            for v in nxt:
                diff = v - target
                if diff < 0:
                    diff = -diff
                if diff < best:
                    best = diff
            cur = nxt
        return best
