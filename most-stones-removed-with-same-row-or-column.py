class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)

        parent = {}
        num_disjoint_sets = 0

        def find(i):
            nonlocal num_disjoint_sets
            if i not in parent:
                parent[i] = i
                num_disjoint_sets += 1
                return i
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal num_disjoint_sets
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                parent[root_i] = root_j
                num_disjoint_sets -= 1
                return True
            return False

        offset = 20000 
        
        for x, y in stones:
            union(x, y + offset)
        
        return n - num_disjoint_sets
