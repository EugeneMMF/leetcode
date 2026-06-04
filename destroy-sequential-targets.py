class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        counts = {}
        for num in nums:
            r = num % space
            if r in counts:
                cnt, mn = counts[r]
                if num < mn:
                    counts[r] = (cnt + 1, num)
                else:
                    counts[r] = (cnt + 1, mn)
            else:
                counts[r] = (1, num)
        max_cnt = 0
        best_seed = None
        for cnt, mn in counts.values():
            if cnt > max_cnt or (cnt == max_cnt and (best_seed is None or mn < best_seed)):
                max_cnt = cnt
                best_seed = mn
        return best_seed