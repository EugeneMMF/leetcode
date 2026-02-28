class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        import bisect
        
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
                
        return len(tails)
