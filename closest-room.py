class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: -x[1])
        indexed_queries = sorted([(minSize, preferred, i) for i, (preferred, minSize) in enumerate(queries)], key=lambda x: -x[0])
        import bisect
        available = []
        ans = [-1] * len(queries)
        r = 0
        for minSize, preferred, idx in indexed_queries:
            while r < len(rooms) and rooms[r][1] >= minSize:
                bisect.insort(available, rooms[r][0])
                r += 1
            if not available:
                continue
            pos = bisect.bisect_left(available, preferred)
            best = None
            if pos < len(available):
                best = available[pos]
            if pos > 0:
                left = available[pos-1]
                if best is None or abs(left-preferred) <= abs(best-preferred) and left < best:
                    best = left
            ans[idx] = best
        return ans
