class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        n = len(nums) // 2
        
        for num, count in counts.items():
            if count == n:
                return num
        return -1

