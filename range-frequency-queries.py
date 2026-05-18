from typing import List, Dict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.indices: Dict[int, List[int]] = {}
        for i, val in enumerate(arr):
            if val in self.indices:
                self.indices[val].append(i)
            else:
                self.indices[val] = [i]

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices:
            return 0
        lst = self.indices[value]
        l = bisect_left(lst, left)
        r = bisect_right(lst, right)
        return r - l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
