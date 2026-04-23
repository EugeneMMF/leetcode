class Solution:
    def getProbability(self, balls):
        from math import comb
        k = len(balls)
        total_balls = sum(balls)
        n = total_balls // 2
        total_comb = comb(total_balls, n)
        ans = 0

        def dfs(idx, taken, weight, distinct1, distinct2):
            nonlocal ans
            if idx == k:
                if taken == n and distinct1 == distinct2:
                    ans += weight
                return
            cnt = balls[idx]
            for take in range(cnt + 1):
                new_taken = taken + take
                if new_taken > n:
                    break
                w = weight * comb(cnt, take)
                d1 = distinct1 + (1 if take > 0 else 0)
                d2 = distinct2 + (1 if cnt - take > 0 else 0)
                dfs(idx + 1, new_taken, w, d1, d2)

        dfs(0, 0, 1, 0, 0)
        return ans / total_comb
