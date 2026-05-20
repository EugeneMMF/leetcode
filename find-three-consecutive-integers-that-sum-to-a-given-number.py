from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        a = num // 3 - 1
        return [a, a + 1, a + 2]
