from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity
        position = -1
        for i, need in enumerate(plants):
            if water < need:
                steps += position - (-1)
                position = -1
                water = capacity
            steps += i - position
            position = i
            water -= need
        return steps
