class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = [0] * m
        moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        for i in range(m):
            r, c = startPos
            count = 0
            for k in range(i, m):
                dr, dc = moves[s[k]]
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    break
                r, c = nr, nc
                count += 1
            ans[i] = count
        return ans
