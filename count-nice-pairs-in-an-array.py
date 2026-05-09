class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def rev(x):
            r = 0
            while x:
                r = r * 10 + x % 10
                x //= 10
            return r
        freq = {}
        for v in nums:
            k = v - rev(v)
            freq[k] = freq.get(k, 0) + 1
        ans = 0
        for c in freq.values():
            ans = (ans + c * (c - 1) // 2) % MOD
        return ans
