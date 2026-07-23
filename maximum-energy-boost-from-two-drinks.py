from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        a = energyDrinkA[0]
        b = energyDrinkB[0]
        s = 0
        for i in range(1, n):
            na = max(a, s) + energyDrinkA[i]
            nb = max(b, s) + energyDrinkB[i]
            ns = max(a, b, s)
            a, b, s = na, nb, ns
        return max(a, b, s)
