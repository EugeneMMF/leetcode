class Solution:
    def trailingZeroes(self, num: int) -> int:
        count = 0
        power_of_5 = 5
        while num >= power_of_5:
            count += num // power_of_5
            power_of_5 *= 5
        return count

    def preimageSizeFZF(self, k: int) -> int:
        low = 0
        high = 5 * 10**9 
        
        ans_x = -1

        while low <= high:
            mid = low + (high - low) // 2
            f_mid = self.trailingZeroes(mid)
            
            if f_mid < k:
                low = mid + 1
            elif f_mid > k:
                high = mid - 1
            else:
                ans_x = mid
                high = mid - 1
        
        if ans_x != -1 and self.trailingZeroes(ans_x) == k:
            return 5
        else:
            return 0
