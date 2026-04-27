class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums) % p
        if total == 0:
            return 0
        need = total
        pref = 0
        best = len(nums) + 1
        seen = {0: -1}
        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref - need) % p
            if target in seen:
                length = i - seen[target]
                if length < best:
                    best = length
            seen[pref] = i
        return best if best < len(nums) else -1
