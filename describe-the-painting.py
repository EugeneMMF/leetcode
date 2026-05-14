class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        events = defaultdict(list)
        for s, e, c in segments:
            events[s].append(('start', c))
            events[e].append(('end', c))
        points = sorted(events.keys())
        res = []
        curr = 0
        prev = None
        for pt in points:
            if prev is not None and prev < pt and curr > 0:
                res.append([prev, pt, curr])
            for typ, col in events[pt]:
                if typ == 'end':
                    curr -= col
            for typ, col in events[pt]:
                if typ == 'start':
                    curr += col
            prev = pt
        return res
