class Solution:
    def countPoints(self, rings: str) -> int:
        masks = [0] * 10
        for i in range(0, len(rings), 2):
            c = rings[i]
            d = int(rings[i + 1])
            if c == 'R':
                masks[d] |= 1
            elif c == 'G':
                masks[d] |= 2
            else:
                masks[d] |= 4
        return sum(1 for m in masks if m == 7)
