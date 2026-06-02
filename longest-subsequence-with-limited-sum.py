class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = []
        s = 0
        for v in nums:
            s += v
            prefix.append(s)
        res = []
        for q in queries:
            lo, hi = 0, len(prefix)
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] <= q:
                    lo = mid + 1
                else:
                    hi = mid
            res.append(lo)
        return res
