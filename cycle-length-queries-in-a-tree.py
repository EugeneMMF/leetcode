class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def depth(v: int) -> int:
            return v.bit_length() - 1
        ans = []
        for a, b in queries:
            da, db = depth(a), depth(b)
            while da > db:
                a //= 2
                da -= 1
            while db > da:
                b //= 2
                db -= 1
            while a != b:
                a //= 2
                b //= 2
                da -= 1
                db -= 1
            lca_depth = da
            dist = depth(queries[ans.__len__()][0]) + depth(queries[ans.__len__()][1]) - 2 * lca_depth
            ans.append(dist + 1)
        return ans