class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        prereq = [0] * n
        for a, b in relations:
            a -= 1
            b -= 1
            prereq[b] |= 1 << a
        full = (1 << n) - 1
        INF = n + 1
        dp = [INF] * (1 << n)
        dp[0] = 0
        from collections import deque
        q = deque([0])
        while q:
            mask = q.popleft()
            if mask == full:
                return dp[mask]
            avail = 0
            for i in range(n):
                if not (mask >> i) & 1 and (prereq[i] & mask) == prereq[i]:
                    avail |= 1 << i
            if avail == 0:
                continue
            cnt = avail.bit_count()
            if cnt <= k:
                nxt = mask | avail
                if dp[nxt] > dp[mask] + 1:
                    dp[nxt] = dp[mask] + 1
                    q.append(nxt)
            else:
                sub = avail
                while sub:
                    if sub.bit_count() <= k:
                        nxt = mask | sub
                        if dp[nxt] > dp[mask] + 1:
                            dp[nxt] = dp[mask] + 1
                            q.append(nxt)
                    sub = (sub - 1) & avail
        return dp[full]
