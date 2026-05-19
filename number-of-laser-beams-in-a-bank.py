from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            count = row.count('1')
            if count:
                if prev:
                    total += prev * count
                prev = count
        return total
