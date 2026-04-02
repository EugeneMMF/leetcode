
class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        target_diff_half = (sumA - sumB) // 2

        bob_candies_set = set(bobSizes)

        for x in aliceSizes:
            y = x - target_diff_half
            if y in bob_candies_set:
                return [x, y]
