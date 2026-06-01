class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        unique_vals = set(nums)
        freq = [0] * 61
        for v in unique_vals:
            pc = v.bit_count()
            freq[pc] += 1
        result = 0
        for p in range(61):
            if freq[p] == 0:
                continue
            for q in range(61):
                if freq[q] == 0:
                    continue
                if p + q >= k:
                    result += freq[p] * freq[q]
        return result
