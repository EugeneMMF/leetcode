class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_time = 0
        for p in left:
            if p > max_time:
                max_time = p
        for p in right:
            t = n - p
            if t > max_time:
                max_time = t
        return max_time
