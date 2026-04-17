class Solution:
    def kConcatenationMaxSum(self, arr, k):
        MOD = 10**9 + 7
        n = len(arr)
        max_ending_here = max_so_far = 0
        for x in arr:
            max_ending_here = max(0, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        if k == 1:
            return max_so_far % MOD
        total = sum(arr)
        max_prefix = cur = 0
        for x in arr:
            cur += x
            max_prefix = max(max_prefix, cur)
        max_suffix = cur = 0
        for x in reversed(arr):
            cur += x
            max_suffix = max(max_suffix, cur)
        max_ending_here = max_so_far2 = 0
        for _ in range(2):
            for x in arr:
                max_ending_here = max(0, max_ending_here + x)
                max_so_far2 = max(max_so_far2, max_ending_here)
        if total > 0:
            ans = max(max_so_far2, max_prefix + max_suffix + (k - 2) * total)
        else:
            ans = max_so_far2
        return ans % MOD
