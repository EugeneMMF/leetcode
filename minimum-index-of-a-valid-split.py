from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt = 1
            elif num == candidate:
                cnt += 1
            else:
                cnt -= 1
        x = candidate
        total = 0
        for num in nums:
            if num == x:
                total += 1
        pref = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == x:
                pref += 1
            L = i + 1
            R = n - L
            if 2 * pref > L and 2 * (total - pref) > R:
                return i
        return -1