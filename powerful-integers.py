from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        xs = [1]
        if x != 1:
            while xs[-1] * x <= bound:
                xs.append(xs[-1] * x)
        ys = [1]
        if y != 1:
            while ys[-1] * y <= bound:
                ys.append(ys[-1] * y)
        res = set()
        for a in xs:
            for b in ys:
                s = a + b
                if s <= bound:
                    res.add(s)
        return list(res)
