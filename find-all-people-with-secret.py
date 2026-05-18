class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        known = set([0, firstPerson])
        i = 0
        m = len(meetings)
        while i < m:
            t = meetings[i][2]
            participants = set()
            edges = []
            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                participants.add(x)
                participants.add(y)
                edges.append((x, y))
                i += 1
            parent = {}
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            def union(a, b):
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[rb] = ra
            for p in participants:
                parent[p] = p
            for a, b in edges:
                union(a, b)
            comp = {}
            for p in participants:
                r = find(p)
                comp.setdefault(r, []).append(p)
            for members in comp.values():
                if any(m in known for m in members):
                    known.update(members)
        return list(known)
