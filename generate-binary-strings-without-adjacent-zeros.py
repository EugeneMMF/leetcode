class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def dfs(pos, prev, cur):
            if pos == n:
                res.append(cur)
                return
            for bit in ('0', '1'):
                if bit == '0' and prev == '0':
                    continue
                dfs(pos + 1, bit, cur + bit)
        dfs(0, '', '')
        return res
