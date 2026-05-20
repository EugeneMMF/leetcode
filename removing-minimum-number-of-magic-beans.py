class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        n = len(beans)
        max_product = 0
        for i, v in enumerate(beans):
            count_ge = n - i
            prod = v * count_ge
            if prod > max_product:
                max_product = prod
        return total - max_product