class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def build(k: int) -> List[List[int]]:
            if k == 0:
                return [[0]]
            sub = build(k - 1)
            m = 1 << k
            half = m >> 1
            count = half * half
            res = [[0] * m for _ in range(m)]
            for i in range(half):
                for j in range(half):
                    val = sub[i][j]
                    res[i][j + half] = val
                    res[i + half][j + half] = val + count
                    res[i + half][j] = val + 2 * count
                    res[i][j] = val + 3 * count
            return res
        return build(n)
