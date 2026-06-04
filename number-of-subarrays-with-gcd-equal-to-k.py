class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        from math import gcd
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == k:
                    ans += 1
                elif cur < k:
                    break
        return ans