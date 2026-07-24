class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        best = None
        for i, s in enumerate(nums):
            outlier = total - 2 * s
            cnt = freq.get(outlier, 0)
            if cnt == 0:
                continue
            if outlier == s and cnt < 2:
                continue
            if best is None or outlier > best:
                best = outlier
        return best
