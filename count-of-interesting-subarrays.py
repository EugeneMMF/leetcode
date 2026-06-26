class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = {}
        prefix_mod = 0
        freq[0] = 1
        ans = 0
        for num in nums:
            if num % modulo == k:
                prefix_mod = (prefix_mod + 1) % modulo
            else:
                prefix_mod = prefix_mod % modulo
            target = (prefix_mod - k) % modulo
            ans += freq.get(target, 0)
            freq[prefix_mod] = freq.get(prefix_mod, 0) + 1
        return ans
