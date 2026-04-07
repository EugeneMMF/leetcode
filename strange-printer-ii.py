class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        for r in range(m):
            for c in range(n):
                colors.add(targetGrid[r][c])

        adj = {color: set() for color in colors}
        pos = {color: [] for color in colors}

        for r in range(m):
            for c in range(n):
                pos[targetGrid[r][c]].append((r, c))

        for color in colors:
            min_r = min(r for r, c in pos[color])
            max_r = max(r for r, c in pos[color])
            min_c = min(c for r, c in pos[color])
            max_c = max(c for r, c in pos[color])

            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    if targetGrid[r][c] != color:
                        adj[targetGrid[r][c]].add(color)

        visited = set()
        recursion_stack = set()

        def dfs(color):
            visited.add(color)
            recursion_stack.add(color)

            for neighbor in adj[color]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
                elif neighbor in recursion_stack:
                    return False

            recursion_stack.remove(color)
            return True

        for color in colors:
            if color not in visited:
                if not dfs(color):
                    return False
        
        return True

