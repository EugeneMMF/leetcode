class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        n = len(flips)
        aligned_count = 0
        current_max_flipped = 0

        for k in range(1, n + 1):
            current_max_flipped = max(current_max_flipped, flips[k - 1])
            if current_max_flipped == k:
                aligned_count += 1

        return aligned_count
