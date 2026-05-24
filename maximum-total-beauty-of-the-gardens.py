class Solution:
    def maximumBeauty(self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        need = [max(0, target - f) for f in flowers]
        pref_need = [0] * (n + 1)
        for i in range(n):
            pref_need[i + 1] = pref_need[i] + need[i]
        pref_flow = [0] * (n + 1)
        for i in range(n):
            pref_flow[i + 1] = pref_flow[i] + flowers[i]
        best = 0
        for full_cnt in range(n + 1):
            cost_full = pref_need[n] - pref_need[n - full_cnt]
            if cost_full > newFlowers:
                continue
            rem = newFlowers - cost_full
            left = n - full_cnt
            if left == 0:
                cur = full_cnt * full
                if cur > best:
                    best = cur
                continue
            if partial == 0:
                cur = full_cnt * full
                if cur > best:
                    best = cur
                continue
            low, high = flowers[0], target - 1
            best_min = 0
            while low <= high:
                mid = (low + high) // 2
                idx = 0
                # find count of gardens among first left that are < mid
                # binary search manually for speed
                l, r = 0, left
                while l < r:
                    m = (l + r) // 2
                    if flowers[m] < mid:
                        l = m + 1
                    else:
                        r = m
                idx = l
                cost = idx * mid - pref_flow[idx]
                if cost <= rem:
                    best_min = mid
                    low = mid + 1
                else:
                    high = mid - 1
            cur = full_cnt * full + best_min * partial
            if cur > best:
                best = cur
        return best