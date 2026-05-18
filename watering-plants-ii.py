class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1
        waterA, waterB = capacityA, capacityB
        refills = 0
        while left <= right:
            if left == right:
                # choose who waters the middle plant
                if waterA >= waterB:
                    if waterA < plants[left]:
                        refills += 1
                        waterA = capacityA
                    waterA -= plants[left]
                else:
                    if waterB < plants[right]:
                        refills += 1
                        waterB = capacityB
                    waterB -= plants[right]
                break
            # Alice waters left plant
            if waterA < plants[left]:
                refills += 1
                waterA = capacityA
            waterA -= plants[left]
            # Bob waters right plant
            if waterB < plants[right]:
                refills += 1
                waterB = capacityB
            waterB -= plants[right]
            left += 1
            right -= 1
        return refills