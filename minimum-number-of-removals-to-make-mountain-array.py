class Solution:
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i] and lds[j] + 1 > lds[i]:
                    lds[i] = lds[j] + 1
        best = 0
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                cur = lis[i] + lds[i] - 1
                if cur > best:
                    best = cur
        return n - best
