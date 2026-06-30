class Solution:
    def numberOfGoodPartitions(self, nums):
        mod = 10**9 + 7
        n = len(nums)
        last_pos = {}
        for i, v in enumerate(nums):
            last_pos[v] = i
        max_last = -1
        cuts = 0
        for i in range(n - 1):
            max_last = max(max_last, last_pos[nums[i]])
            if max_last == i:
                cuts += 1
        return pow(2, cuts, mod)
