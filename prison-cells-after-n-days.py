class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n:
            key = tuple(cells)
            if key in seen:
                n %= seen[key] - n
            seen[key] = n
            if n:
                n -= 1
                new = [0] * 8
                for i in range(1, 7):
                    new[i] = 1 if cells[i - 1] == cells[i + 1] else 0
                cells = new
        return cells
