class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        max_val = (1 << 30) - 1
        best = {}
        for i in range(n):
            val = 0
            for j in range(i, min(n, i + 30)):
                val = (val << 1) | (s[j] == '1')
                if val > max_val:
                    break
                length = j - i + 1
                if val not in best or length < best[val][0] or (length == best[val][0] and i < best[val][1]):
                    best[val] = (length, i, j)
        res = []
        for first, second in queries:
            target = first ^ second
            if target in best:
                _, l, r = best[target]
                res.append([l, r])
            else:
                res.append([-1, -1])
        return res