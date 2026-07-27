class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        import bisect
        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        res = []
        for idx in queries:
            v = nums[idx]
            lst = pos[v]
            if len(lst) <= 1:
                res.append(-1)
                continue
            i = idx
            p = bisect.bisect_right(lst, i)
            next_idx = lst[p] if p < len(lst) else lst[0]
            p2 = bisect.bisect_left(lst, i)
            prev_idx = lst[p2 - 1] if p2 > 0 else lst[-1]
            dist1 = (next_idx - i) % n
            dist2 = (i - prev_idx) % n
            res.append(min(dist1, dist2))
        return res
