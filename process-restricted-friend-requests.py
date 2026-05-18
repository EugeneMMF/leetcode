class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        size = [1] * n
        restricted = {i: set() for i in range(n)}
        for x, y in restrictions:
            restricted[x].add(y)
            restricted[y].add(x)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(u: int, v: int) -> bool:
            ru, rv = find(u), find(v)
            if ru == rv:
                return True
            if rv in restricted[ru] or ru in restricted[rv]:
                return False
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            for r in restricted[rv]:
                restricted[ru].add(r)
                restricted[r].remove(rv)
                restricted[r].add(ru)
            del restricted[rv]
            return True

        result = []
        for u, v in requests:
            result.append(union(u, v))
        return result