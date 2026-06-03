class Solution:
    def componentValue(self, nums, edges):
        from collections import defaultdict
        n = len(nums)
        if n == 1:
            return 0
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        total = sum(nums)
        divisors = []
        i = 1
        while i * i <= total:
            if total % i == 0:
                divisors.append(i)
                if i * i != total:
                    divisors.append(total // i)
            i += 1
        divisors.sort()
        import sys
        sys.setrecursionlimit(30000)
        def can(target):
            cuts = 0
            def dfs(u, p, is_root):
                nonlocal cuts
                s = nums[u]
                for v in g[u]:
                    if v == p:
                        continue
                    s += dfs(v, u, False)
                if s == target:
                    if not is_root:
                        cuts += 1
                    return 0
                return s
            dfs(0, -1, True)
            return cuts == total // target - 1
        for t in divisors:
            if t == total:
                continue
            if can(t):
                return total // t - 1
        return 0