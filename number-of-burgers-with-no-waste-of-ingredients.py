class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        if (tomatoSlices % 2 != 0 or
            tomatoSlices < 2 * cheeseSlices or
            tomatoSlices > 4 * cheeseSlices):
            return []

        total_jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        total_small = cheeseSlices - total_jumbo

        return [total_jumbo, total_small]
