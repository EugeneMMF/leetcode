from typing import List

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.price_map = {p: pr for p, pr in zip(products, prices)}
        self.counter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        total = 0
        for p, a in zip(product, amount):
            total += self.price_map[p] * a
        if self.counter % self.n == 0:
            total = total * (100 - self.discount) / 100
        return float(total)

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
