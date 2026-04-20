from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        s = sum(arr[:k])
        cnt = 1 if s >= target else 0
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            if s >= target:
                cnt += 1
        return cnt
