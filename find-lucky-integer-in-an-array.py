from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        ans = -1
        for num, cnt in freq.items():
            if num == cnt and num > ans:
                ans = num
        return ans
