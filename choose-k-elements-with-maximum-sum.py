class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums1)
        idxs = sorted(range(n), key=lambda i: nums1[i])
        top = []
        sum_top = 0
        ans = [0] * n
        i = 0
        while i < n:
            val = nums1[idxs[i]]
            group = []
            while i < n and nums1[idxs[i]] == val:
                group.append(idxs[i])
                i += 1
            for idx in group:
                ans[idx] = sum_top
            for idx in group:
                v = nums2[idx]
                heapq.heappush(top, v)
                sum_top += v
                if len(top) > k:
                    smallest = heapq.heappop(top)
                    sum_top -= smallest
        return ans
