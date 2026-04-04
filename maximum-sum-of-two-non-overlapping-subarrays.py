class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        def get_sum(l, r):
            return prefix_sum[r+1] - prefix_sum[l]

        max_sum = 0

        for i in range(n - firstLen + 1):
            sum1 = get_sum(i, i + firstLen - 1)
            for j in range(n - secondLen + 1):
                sum2 = get_sum(j, j + secondLen - 1)
                if (j >= i + firstLen) or (i >= j + secondLen):
                    max_sum = max(max_sum, sum1 + sum2)
        
        return max_sum
