class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        rank = [0]*n
        def find(x):
            while parent[x]!=x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            ra,rb = find(a),find(b)
            if ra==rb: return
            if rank[ra]<rank[rb]:
                parent[ra]=rb
            elif rank[ra]>rank[rb]:
                parent[rb]=ra
            else:
                parent[rb]=ra
                rank[ra]+=1
        idxs = sorted(range(n), key=lambda i: nums[i])
        for k in range(n-1):
            i,j = idxs[k], idxs[k+1]
            if abs(nums[i]-nums[j])<=limit:
                union(i,j)
        comp = {}
        for i in range(n):
            r = find(i)
            comp.setdefault(r, []).append(i)
        res = [0]*n
        for indices in comp.values():
            vals = [nums[i] for i in indices]
            indices.sort()
            vals.sort()
            for i,val in zip(indices, vals):
                res[i]=val
        return res