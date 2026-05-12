class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        keys = sorted(freq)
        ops = 0
        for i, val in enumerate(keys):
            if i == 0:
                continue
            ops += freq[val] * i
        return ops
