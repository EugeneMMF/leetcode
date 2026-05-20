class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        for mask in range(1 << n):
            ok = True
            for i in range(n):
                if (mask >> i) & 1:
                    for j in range(n):
                        if statements[i][j] == 2:
                            continue
                        if statements[i][j] == 1:
                            if not ((mask >> j) & 1):
                                ok = False
                                break
                        else:
                            if (mask >> j) & 1:
                                ok = False
                                break
                if not ok:
                    break
            if ok:
                cnt = bin(mask).count("1")
                if cnt > max_good:
                    max_good = cnt
        return max_good