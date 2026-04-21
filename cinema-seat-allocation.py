class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict
        rows = defaultdict(int)
        for r, s in reservedSeats:
            rows[r] |= 1 << (s - 1)
        total = (n - len(rows)) * 2
        left_mask = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)
        middle_mask = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6)
        right_mask = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)
        for mask in rows.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            if left_free and right_free:
                total += 2
            elif left_free or right_free or (mask & middle_mask) == 0:
                total += 1
        return total
