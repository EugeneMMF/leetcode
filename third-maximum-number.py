class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max1 = None
        max2 = None
        max3 = None

        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue

            if max1 is None or num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 is None or num > max2:
                max3 = max2
                max2 = num
            elif max3 is None or num > max3:
                max3 = num
        
        if max3 is None:
            return max1
        else:
            return max3
