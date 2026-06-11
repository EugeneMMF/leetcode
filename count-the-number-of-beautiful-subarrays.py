class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        freq = {}
        pref = 0
        ans = 0
        freq[0] = 1
        for num in nums:
            pref ^= num
            cnt = freq.get(pref, 0)
            ans += cnt
            freq[pref] = cnt + 1
        return ans
