import math

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first_num = math.inf
        second_num = math.inf

        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True
        
        return False
