from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        n = len(cookies)
        sums = [0] * k
        best = sum(cookies)

        def dfs(idx, cur_max):
            nonlocal best
            if idx == n:
                if cur_max < best:
                    best = cur_max
                return
            if cur_max >= best:
                return
            seen = set()
            for i in range(k):
                if sums[i] in seen:
                    continue
                seen.add(sums[i])
                new_sum = sums[i] + cookies[idx]
                sums[i] = new_sum
                dfs(idx + 1, max(cur_max, new_sum))
                sums[i] -= cookies[idx]
                if sums[i] == 0:
                    break

        dfs(0, 0)
        return best
