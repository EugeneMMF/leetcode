from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr
