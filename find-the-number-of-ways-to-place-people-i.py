class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                if xi <= xj and yi >= yj and not (xi == xj and yi == yj):
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if xi <= xk <= xj and yj <= yk <= yi:
                            ok = False
                            break
                    if ok:
                        count += 1
        return count
