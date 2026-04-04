class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        remainder_counts = [0] * 60
        count = 0

        for t in time:
            rem = t % 60
            
            complement_rem = (60 - rem) % 60
            
            count += remainder_counts[complement_rem]
            
            remainder_counts[rem] += 1
            
        return count
