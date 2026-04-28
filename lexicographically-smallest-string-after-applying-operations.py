class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque
        n = len(s)
        seen = {s}
        q = deque([s])
        best = s
        while q:
            cur = q.popleft()
            if cur < best:
                best = cur
            lst = list(cur)
            for i in range(1, n, 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            added = ''.join(lst)
            if added not in seen:
                seen.add(added)
                q.append(added)
            rotated = cur[-b:] + cur[:-b]
            if rotated not in seen:
                seen.add(rotated)
                q.append(rotated)
        return best
