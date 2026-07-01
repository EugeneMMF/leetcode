class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        best = None
        min_pref = {}
        for j in range(n):
            target1 = nums[j] + k
            if target1 in min_pref:
                s = prefix[j + 1] - min_pref[target1]
                if best is None or s > best:
                    best = s
            target2 = nums[j] - k
            if target2 in min_pref:
                s = prefix[j + 1] - min_pref[target2]
                if best is None or s > best:
                    best = s
            val = nums[j]
            if val not in min_pref or prefix[j] < min_pref[val]:
                min_pref[val] = prefix[j]
        return 0 if best is None else best