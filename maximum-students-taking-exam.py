class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        valid_masks = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)
            row_masks = []
            sub = mask
            while True:
                if (sub & (sub << 1)) == 0:
                    row_masks.append(sub)
                if sub == 0:
                    break
                sub = (sub - 1) & mask
            valid_masks.append(row_masks)
        dp = {}
        for mask in valid_masks[0]:
            dp[mask] = bin(mask).count('1')
        for r in range(1, m):
            new_dp = {}
            for mask in valid_masks[r]:
                cur = bin(mask).count('1')
                for prev_mask, val in dp.items():
                    if (mask & (prev_mask << 1)) == 0 and (mask & (prev_mask >> 1)) == 0:
                        total = val + cur
                        if mask not in new_dp or total > new_dp[mask]:
                            new_dp[mask] = total
                if not dp:
                    new_dp[mask] = cur
            dp = new_dp
        return max(dp.values()) if dp else 0
