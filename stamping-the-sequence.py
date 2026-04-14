class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        t = list(target)
        visited = [False] * (n - m + 1)
        ans = []
        total = 0
        def can_stamp(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != stamp[j]:
                    return False
                changed = True
            return changed
        def do_stamp(i):
            nonlocal total
            for j in range(m):
                if t[i + j] != '?':
                    t[i + j] = '?'
                    total += 1
        while total < n:
            progress = False
            for i in range(n - m + 1):
                if not visited[i] and can_stamp(i):
                    do_stamp(i)
                    visited[i] = True
                    ans.append(i)
                    progress = True
            if not progress:
                break
        return ans[::-1] if total == n else []
