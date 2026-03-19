class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_hamming_distance = 0
        
        # Iterate over each bit position.
        # For numbers up to 10^9, we need to consider bits from 0 to 29.
        # An iteration range of 30 covers bits 0 through 29.
        for k in range(30):
            count_0 = 0
            count_1 = 0
            
            # Count numbers with 0 at the k-th bit and 1 at the k-th bit
            for num in nums:
                if (num >> k) & 1:
                    count_1 += 1
                else:
                    count_0 += 1
            
            # The number of pairs with different k-th bits is count_0 * count_1.
            # Each such pair contributes 1 to the total Hamming distance for this bit position.
            total_hamming_distance += count_0 * count_1
            
        return total_hamming_distance
