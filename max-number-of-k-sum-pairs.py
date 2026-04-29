class Solution:
    def maxOperations(self, nums, k):
        from collections import Counter
        cnt = Counter(nums)
        ops = 0
        for x in list(cnt.keys()):
            y = k - x
            if y not in cnt:
                continue
            if x == y:
                pairs = cnt[x] // 2
                ops += pairs
                cnt[x] -= pairs * 2
            elif x < y:
                pairs = min(cnt[x], cnt[y])
                ops += pairs
                cnt[x] -= pairs
                cnt[y] -= pairs
        return ops
