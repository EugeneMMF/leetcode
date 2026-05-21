class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_points = -1
        best_used = 0
        best_mask = 0
        for mask in range(1 << 12):
            used = 0
            points = 0
            for k in range(12):
                if mask & (1 << k):
                    used += aliceArrows[k] + 1
                    points += k
            if used <= numArrows and points > best_points:
                best_points = points
                best_used = used
                best_mask = mask
        bobArrows = [0] * 12
        for k in range(12):
            if best_mask & (1 << k):
                bobArrows[k] = aliceArrows[k] + 1
        remaining = numArrows - best_used
        bobArrows[0] += remaining
        return bobArrows
