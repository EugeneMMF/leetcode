class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)
        max_moves = max(stones[-1] - stones[1] - (n - 2), stones[-2] - stones[0] - (n - 2))
        left = 0
        best = 0
        for right in range(n):
            while stones[right] - stones[left] >= n:
                left += 1
            best = max(best, right - left + 1)
        if best == n - 1:
            if (stones[n-2] - stones[0] == n - 2 and stones[-1] - stones[-2] > 2) or (stones[-1] - stones[1] == n - 2 and stones[1] - stones[0] > 2):
                min_moves = 2
            else:
                min_moves = 1
        else:
            min_moves = n - best
        return [min_moves, max_moves]
