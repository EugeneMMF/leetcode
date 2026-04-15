class Solution:
    def gridIllumination(self, n, lamps, queries):
        from collections import defaultdict
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)
        anti = defaultdict(int)
        lamps_set = set()
        for r, c in lamps:
            if (r, c) in lamps_set:
                continue
            lamps_set.add((r, c))
            row[r] += 1
            col[c] += 1
            diag[r - c] += 1
            anti[r + c] += 1
        ans = []
        for r, c in queries:
            if row[r] or col[c] or diag[r - c] or anti[r + c]:
                ans.append(1)
            else:
                ans.append(0)
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in lamps_set:
                        lamps_set.remove((nr, nc))
                        row[nr] -= 1
                        if row[nr] == 0:
                            del row[nr]
                        col[nc] -= 1
                        if col[nc] == 0:
                            del col[nc]
                        diag[nr - nc] -= 1
                        if diag[nr - nc] == 0:
                            del diag[nr - nc]
                        anti[nr + nc] -= 1
                        if anti[nr + nc] == 0:
                            del anti[nr + nc]
        return ans
