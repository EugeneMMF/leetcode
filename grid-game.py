class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = grid[0]
        bottom = grid[1]
        suffTop = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffTop[i] = suffTop[i + 1] + top[i]
        prefBottom = [0] * n
        prefBottom[0] = bottom[0]
        for i in range(1, n):
            prefBottom[i] = prefBottom[i - 1] + bottom[i]
        ans = float('inf')
        for k in range(n):
            left = prefBottom[k - 1] if k > 0 else 0
            right = suffTop[k + 1] if k + 1 < n else 0
            ans = min(ans, max(left, right))
        return ans
