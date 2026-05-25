class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_gap = 0
        # gap before first special
        first_gap = special[0] - bottom
        if first_gap > max_gap:
            max_gap = first_gap
        # gaps between specials
        for i in range(1, len(special)):
            gap = special[i] - special[i - 1] - 1
            if gap > max_gap:
                max_gap = gap
        # gap after last special
        last_gap = top - special[-1]
        if last_gap > max_gap:
            max_gap = last_gap
        return max_gap
