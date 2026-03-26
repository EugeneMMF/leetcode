class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 1
        high = m * n
        
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            count = 0
            for i in range(1, m + 1):
                count += min(n, mid // i)
            
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
