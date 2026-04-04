class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(capacity: int) -> bool:
            days_needed = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
            return days_needed <= days

        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
