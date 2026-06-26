class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        targets = ["00", "25", "50", "75"]
        best = n
        for t in targets:
            j = -1
            i = -1
            for idx in range(n-1, -1, -1):
                if num[idx] == t[1]:
                    j = idx
                    break
            if j == -1:
                continue
            for idx in range(j-1, -1, -1):
                if num[idx] == t[0]:
                    i = idx
                    break
            if i == -1:
                continue
            deletions = (n-1 - j) + (j-1 - i)
            if deletions < best:
                best = deletions
        if best == n:
            if '0' in num:
                best = n - 1
        return best