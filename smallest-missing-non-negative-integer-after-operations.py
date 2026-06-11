class Solution:
    def findSmallestInteger(self, nums, value):
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1
        used = [0] * value
        m = 0
        while True:
            r = m % value
            if used[r] < cnt[r]:
                used[r] += 1
                m += 1
            else:
                break
        return m
