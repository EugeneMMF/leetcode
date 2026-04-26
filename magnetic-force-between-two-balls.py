from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        def can(dist):
            count = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= dist:
                    count += 1
                    last = p
                    if count >= m:
                        return True
            return False
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
