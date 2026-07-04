class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        n = len(sorted1)
        ans = 10**9
        for i in range(n):
            for j in range(i + 1, n):
                x = None
                k1 = 0
                ok = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    diff = sorted2[k1] - sorted1[k]
                    if x is None:
                        x = diff
                    elif diff != x:
                        ok = False
                        break
                    k1 += 1
                if ok:
                    ans = min(ans, x)
        return ans
