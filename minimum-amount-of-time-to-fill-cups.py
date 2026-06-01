class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a, b, c = amount
        x, y, z = sorted((a, b, c), reverse=True)
        if x > y + z:
            return x
        return (x + y + z + 1) // 2