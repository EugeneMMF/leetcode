class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff = [0] * 101
        for b, d in logs:
            diff[b - 1950] += 1
            diff[d - 1950] -= 1
        max_pop = 0
        year = 1950
        cur = 0
        for i in range(101):
            cur += diff[i]
            if cur > max_pop:
                max_pop = cur
                year = 1950 + i
        return year