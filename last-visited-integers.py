from typing import List

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for num in nums:
            if num == -1:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
            else:
                seen.insert(0, num)
                k = 0
        return ans
