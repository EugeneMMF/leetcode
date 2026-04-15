from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [0] * 26
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - 97
                b = ord(eq[3]) - 97
                union(a, b)
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - 97
                b = ord(eq[3]) - 97
                if find(a) == find(b):
                    return False
        return True
