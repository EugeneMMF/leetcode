class Solution:
    def queensAttacktheKing(self, queens, king):
        qset = {tuple(q) for q in queens}
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        res = []
        xk, yk = king
        for dx, dy in dirs:
            x, y = xk + dx, yk + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in qset:
                    res.append([x, y])
                    break
                x += dx
                y += dy
        return res
