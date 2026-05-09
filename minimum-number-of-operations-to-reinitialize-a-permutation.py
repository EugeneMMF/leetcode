class Solution:
    def reinitializePermutation(self, n: int) -> int:
        p = [0] * n
        for i in range(n):
            if i % 2 == 0:
                j = i // 2
            else:
                j = n // 2 + (i - 1) // 2
            p[j] = i
        from math import gcd
        lcm = 1
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                cur = i
                cycle_len = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = p[cur]
                    cycle_len += 1
                lcm = lcm * cycle_len // gcd(lcm, cycle_len)
        return lcm
