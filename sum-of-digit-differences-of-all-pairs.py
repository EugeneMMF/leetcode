class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        k = len(str(nums[0]))
        total_diff = 0
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = pow10[i - 1] * 10
        for pos in range(k):
            count = [0] * 10
            div = pow10[k - pos - 1]
            for num in nums:
                digit = (num // div) % 10
                count[digit] += 1
            for c in count:
                total_diff += c * (n - c)
        return total_diff // 2