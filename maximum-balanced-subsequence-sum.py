class Solution:
    def maxBalancedSubsequenceSum(self, nums):
        n = len(nums)
        keys = [nums[i] - i for i in range(n)]
        uniq = sorted(set(keys))
        comp = {v: i + 1 for i, v in enumerate(uniq)}
        size = len(uniq) + 2
        tree = [-10**18] * size
        def update(i, val):
            while i < size:
                if val > tree[i]:
                    tree[i] = val
                i += i & -i
        def query(i):
            res = -10**18
            while i > 0:
                if tree[i] > res:
                    res = tree[i]
                i -= i & -i
            return res
        max_sum = -10**18
        for i in range(n):
            idx = comp[keys[i]]
            best = query(idx)
            if best < 0:
                best = 0
            dp = nums[i] + best
            update(idx, dp)
            if dp > max_sum:
                max_sum = dp
        return max_sum