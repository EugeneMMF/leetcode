class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)
        for i in range(n):
            seg[size + i] = heights[i]
        for i in range(size - 1, 0, -1):
            seg[i] = seg[2 * i] if seg[2 * i] > seg[2 * i + 1] else seg[2 * i + 1]
        def first_greater(l, t):
            if l >= n:
                return -1
            def dfs(node, nl, nr):
                if nr <= l or seg[node] <= t:
                    return -1
                if nl + 1 == nr:
                    return nl
                mid = (nl + nr) // 2
                left = dfs(node * 2, nl, mid)
                if left != -1:
                    return left
                return dfs(node * 2 + 1, mid, nr)
            return dfs(1, 0, size)
        ans = []
        for a, b in queries:
            if a == b:
                ans.append(a)
                continue
            if a < b and heights[a] < heights[b]:
                ans.append(b)
                continue
            if b < a and heights[b] < heights[a]:
                ans.append(a)
                continue
            l = max(a, b) + 1
            t = max(heights[a], heights[b])
            res = first_greater(l, t)
            ans.append(res)
        return ans