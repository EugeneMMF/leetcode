class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [True] * n
        for i in range(1, n):
            pref[i] = pref[i-1] and nums[i-1] < nums[i]
        suff = [True] * n
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] and nums[i] < nums[i+1]
        good = [(nums[j], j) for j in range(1, n) if suff[j]]
        good.sort(reverse=True)
        queries = []
        for l in range(n):
            if l > 0 and not pref[l-1]:
                continue
            threshold = nums[l-1] if l > 0 else -1
            queries.append((threshold, l))
        queries.sort(reverse=True)
        class BIT:
            def __init__(self, size):
                self.n = size
                self.bit = [0]*(size+1)
            def add(self, i, v):
                i += 1
                while i <= self.n:
                    self.bit[i] += v
                    i += i & -i
            def sum(self, i):
                s = 0
                i += 1
                while i>0:
                    s += self.bit[i]
                    i -= i & -i
                return s
            def range_sum(self, l, r):
                return self.sum(r) - (self.sum(l-1) if l>0 else 0)
        bit = BIT(n)
        ans = 0
        idx = 0
        for threshold, l in queries:
            while idx < len(good) and good[idx][0] > threshold:
                bit.add(good[idx][1], 1)
                idx += 1
            r_start = l+1
            r_end = n-1
            if r_start <= r_end:
                ans += bit.range_sum(r_start, r_end)
            ans += 1
        return ans
