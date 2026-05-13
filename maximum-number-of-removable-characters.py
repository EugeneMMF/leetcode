class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        removed = [False] * n
        def can(k: int) -> bool:
            for i in range(k):
                removed[removable[i]] = True
            j = 0
            for i in range(n):
                if removed[i]:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1
                    if j == len(p):
                        break
            for i in range(k):
                removed[removable[i]] = False
            return j == len(p)
        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
