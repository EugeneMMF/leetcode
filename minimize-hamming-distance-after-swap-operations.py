class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))
        size = [1]*n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb: return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        for a,b in allowedSwaps:
            union(a,b)
        comp_map = {}
        for i in range(n):
            r = find(i)
            if r not in comp_map:
                comp_map[r] = [[],[]]
            comp_map[r][0].append(source[i])
            comp_map[r][1].append(target[i])
        ans = 0
        for src_vals, tgt_vals in comp_map.values():
            freq = {}
            for v in src_vals:
                freq[v] = freq.get(v,0)+1
            for v in tgt_vals:
                if freq.get(v,0):
                    freq[v] -= 1
                else:
                    ans += 1
        return ans
