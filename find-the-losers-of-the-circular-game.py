from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = set()
        current = 1
        step = 1
        while True:
            if current in visited:
                break
            visited.add(current)
            current = ((current - 1 + step * k) % n) + 1
            step += 1
        return [i for i in range(1, n+1) if i not in visited]
