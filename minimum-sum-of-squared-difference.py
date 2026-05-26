class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        freq = {}
        maxd = 0
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d:
                freq[d] = freq.get(d, 0) + 1
                if d > maxd:
                    maxd = d
        K = k1 + k2
        d = maxd
        while d > 0 and K > 0:
            cnt = freq.get(d, 0)
            if cnt == 0:
                d -= 1
                continue
            if K >= cnt:
                K -= cnt
                freq[d] = 0
                freq[d-1] = freq.get(d-1, 0) + cnt
            else:
                freq[d] -= K
                freq[d-1] = freq.get(d-1, 0) + K
                K = 0
            d -= 1
        res = 0
        for diff, cnt in freq.items():
            res += diff * diff * cnt
        return res
