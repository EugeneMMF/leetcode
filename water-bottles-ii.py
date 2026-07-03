class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        full = numBottles
        empty = 0
        current = numExchange
        while full > 0 or empty >= current:
            if full > 0:
                total += full
                empty += full
                full = 0
            if empty >= current:
                empty -= current
                full += 1
                current += 1
        return total