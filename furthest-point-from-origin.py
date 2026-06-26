class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        base = 0
        k = 0
        for c in moves:
            if c == 'L':
                base -= 1
            elif c == 'R':
                base += 1
            else:
                k += 1
        return max(abs(base - k), abs(base + k))
