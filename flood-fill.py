class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or image[r][c] != original_color:
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image
