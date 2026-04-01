class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        
        parent = list(range(n))
        rank = [0] * n
        num_components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_j] < rank[root_i]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                
                nonlocal num_components
                num_components -= 1
                return True
            return False

        def are_similar(s1, s2):
            diffs = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diffs.append(i)
            
            if len(diffs) == 0:
                return True
            
            if len(diffs) == 2:
                p1, p2 = diffs[0], diffs[1]
                if s1[p1] == s2[p2] and s1[p2] == s2[p1]:
                    return True
                    
            return False

        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    union(i, j)
        
        return num_components

