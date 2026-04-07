class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        for i in range(n):
            left_count = i + 1
            right_count = n - i
            total_combinations = left_count * right_count
            odd_combinations = (total_combinations + 1) // 2
            total_sum += arr[i] * odd_combinations
        return total_sum
