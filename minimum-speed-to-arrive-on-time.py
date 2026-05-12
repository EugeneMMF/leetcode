class Solution:
    def minSpeedOnTime(self, dist, hour):
        n = len(dist)
        if hour < n - 1:
            return -1
        def feasible(speed):
            total = 0
            for d in dist[:-1]:
                total += (d + speed - 1) // speed
            total += dist[-1] / speed
            return total <= hour + 1e-9
        low, high = 1, 10**7
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low if feasible(low) else -1