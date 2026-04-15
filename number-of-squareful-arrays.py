class Solution:
    def numSquarefulPerms(self, nums):
        import math
        n = len(nums)
        nums.sort()
        visited = [False] * n
        ans = 0
        def is_square(x):
            r = int(math.isqrt(x))
            return r * r == x
        def dfs(pos, last):
            nonlocal ans
            if pos == n:
                ans += 1
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if pos == 0 or is_square(nums[i] + last):
                    visited[i] = True
                    dfs(pos + 1, nums[i])
                    visited[i] = False
        dfs(0, 0)
        return ans
