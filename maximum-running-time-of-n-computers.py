class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        low, high = 0, total // n
        while low < high:
            mid = (low + high + 1) // 2
            used = 0
            for b in batteries:
                used += b if b < mid else mid
                if used >= n * mid:
                    break
            if used >= n * mid:
                low = mid
            else:
                high = mid - 1
        return low