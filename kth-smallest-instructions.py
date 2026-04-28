class Solution:
    def kthSmallestPath(self, destination, k):
        from math import comb
        row, col = destination
        h, v = col, row
        res = []
        while h > 0 or v > 0:
            if h == 0:
                res.append('V')
                v -= 1
            elif v == 0:
                res.append('H')
                h -= 1
            else:
                cnt = comb(h + v - 1, h - 1)
                if k <= cnt:
                    res.append('H')
                    h -= 1
                else:
                    res.append('V')
                    k -= cnt
                    v -= 1
        return ''.join(res)
