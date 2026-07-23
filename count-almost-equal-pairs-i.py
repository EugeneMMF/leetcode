from typing import List

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        swap_sets = [set() for _ in range(n)]
        for idx, num in enumerate(nums):
            s = list(str(num))
            L = len(s)
            seen = set()
            for i in range(L):
                for j in range(i + 1, L):
                    s2 = s.copy()
                    s2[i], s2[j] = s2[j], s2[i]
                    v = int(''.join(s2))
                    if v != num:
                        seen.add(v)
            swap_sets[idx] = seen
        cnt = 0
        for i in range(n):
            xi = nums[i]
            for j in range(i + 1, n):
                yj = nums[j]
                if xi == yj or yj in swap_sets[i] or xi in swap_sets[j]:
                    cnt += 1
        return cnt
