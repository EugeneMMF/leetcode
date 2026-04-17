class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        forward = [0] * n
        backward = [0] * n
        forward[0] = arr[0]
        max_sum = arr[0]
        for i in range(1, n):
            forward[i] = max(arr[i], forward[i-1] + arr[i])
            if forward[i] > max_sum:
                max_sum = forward[i]
        backward[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            backward[i] = max(arr[i], backward[i+1] + arr[i])
        for i in range(1, n-1):
            combined = forward[i-1] + backward[i+1]
            if combined > max_sum:
                max_sum = combined
        return max_sum
