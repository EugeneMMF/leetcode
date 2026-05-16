class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        from bisect import bisect_right, bisect_left
        def count_le(x):
            cnt = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        cnt += len(nums2)
                elif a > 0:
                    cnt += bisect_right(nums2, x // a)
                else:
                    ceil_div = -((-x) // a)
                    cnt += len(nums2) - bisect_left(nums2, ceil_div)
            return cnt
        low = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        high = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low