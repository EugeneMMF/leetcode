class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        total_masks = 1 << n
        sum_mask = [0] * total_masks
        for mask in range(1, total_masks):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            sum_mask[mask] = sum_mask[mask ^ lsb] + tasks[idx]
        valid_subsets = [mask for mask in range(total_masks) if sum_mask[mask] <= sessionTime]
        INF = n + 1
        dp = [INF] * total_masks
        dp[0] = 0
        for mask in range(total_masks):
            cur = dp[mask]
            if cur == INF:
                continue
            for sub in valid_subsets:
                if sub & mask == 0:
                    newmask = mask | sub
                    if dp[newmask] > cur + 1:
                        dp[newmask] = cur + 1
        return dp[total_masks - 1]