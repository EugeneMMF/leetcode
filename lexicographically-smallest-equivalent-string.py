class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - 97, ord(c2) - 97)
        res = []
        for ch in baseStr:
            res.append(chr(find(ord(ch) - 97) + 97))
        return ''.join(res)
