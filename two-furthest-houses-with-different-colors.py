class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        first_color = colors[0]
        last_color = colors[-1]
        dist1 = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != first_color:
                dist1 = j
                break
        dist2 = 0
        for i in range(n):
            if colors[i] != last_color:
                dist2 = n - 1 - i
                break
        return max(dist1, dist2)
