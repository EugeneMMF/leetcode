from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        presence = set(nums)
        dp = {}
        max_len = 1
        for num in sorted(presence):
            root = int(num**0.5)
            if root * root == num and root in presence:
                dp[num] = dp.get(root, 1) + 1
            else:
                dp[num] = 1
            if dp[num] > max_len:
                max_len = dp[num]
        return max_len if max_len >= 2 else -1
