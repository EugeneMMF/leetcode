class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        seeds = sorted(zip(growTime, plantTime), reverse=True)
        cur = 0
        ans = 0
        for grow, plant in seeds:
            cur += plant
            if cur + grow > ans:
                ans = cur + grow
        return ans
