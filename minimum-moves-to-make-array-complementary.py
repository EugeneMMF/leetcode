class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        m = n // 2
        size = 2 * limit + 2
        diff = [0] * (size + 1)
        exact = [0] * (size + 1)
        for i in range(m):
            a = nums[i]
            b = nums[n - 1 - i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            diff[low] += 1
            diff[high + 1] -= 1
            exact[a + b] += 1
        best = 2 * m
        cur = 0
        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            moves = 2 * m - cur - exact[s]
            if moves < best:
                best = moves
        return best
