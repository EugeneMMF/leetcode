class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n < 3:
            return False
        a_removals = 0
        b_removals = 0
        for i in range(1, n - 1):
            if colors[i] == 'A' and colors[i - 1] == 'A' and colors[i + 1] == 'A':
                a_removals += 1
            elif colors[i] == 'B' and colors[i - 1] == 'B' and colors[i + 1] == 'B':
                b_removals += 1
        return a_removals > b_removals