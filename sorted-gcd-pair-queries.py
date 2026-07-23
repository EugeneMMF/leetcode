class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for v in nums:
            cnt[v] += 1
        m = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            s = 0
            for k in range(d, max_val + 1, d):
                s += cnt[k]
            m[d] = s
        exact = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total_pairs = m[d] * (m[d] - 1) // 2
            sub = 0
            for k in range(2 * d, max_val + 1, d):
                sub += exact[k]
            exact[d] = total_pairs - sub
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        ans = [0] * len(queries)
        cur = 0
        d = 1
        for idx, q in sorted_queries:
            while cur <= q:
                cur += exact[d]
                d += 1
            ans[idx] = d - 1
        return ans
