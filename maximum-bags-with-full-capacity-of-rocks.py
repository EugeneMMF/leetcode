class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needed = [c - r for c, r in zip(capacity, rocks)]
        needed.sort()
        count = 0
        for req in needed:
            if req <= additionalRocks:
                additionalRocks -= req
                count += 1
            else:
                break
        return count