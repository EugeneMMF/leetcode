class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        cnt = {}
        pairs = 0
        l = 0
        ans = 0
        for r in range(n):
            v = nums[r]
            pairs += cnt.get(v, 0)
            cnt[v] = cnt.get(v, 0) + 1
            while pairs >= k:
                ans += n - r
                lv = nums[l]
                cnt[lv] -= 1
                pairs -= cnt[lv]
                l += 1
        return ans
