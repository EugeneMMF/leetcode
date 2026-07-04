class Solution:
    def medianOfUniquenessArray(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        k = (total + 1) // 2
        def count_leq(limit):
            freq = {}
            distinct = 0
            left = 0
            res = 0
            for right, val in enumerate(nums):
                if freq.get(val, 0) == 0:
                    distinct += 1
                freq[val] = freq.get(val, 0) + 1
                while distinct > limit:
                    lv = nums[left]
                    freq[lv] -= 1
                    if freq[lv] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo