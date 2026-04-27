class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0
        for i, val in enumerate(arr):
            left = i + 1
            right = n - i
            total += val * ((left * right + 1) // 2)
        return total
