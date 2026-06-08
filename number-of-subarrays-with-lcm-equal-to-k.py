class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        from math import gcd
        n=len(nums)
        count=0
        for i in range(n):
            lcm=1
            for j in range(i,n):
                lcm=lcm//gcd(lcm,nums[j])*nums[j]
                if lcm>k:
                    break
                if lcm==k:
                    count+=1
        return count