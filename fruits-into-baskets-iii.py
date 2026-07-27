import typing

class Solution:
    def numOfUnplacedFruits(self, fruits: typing.List[int], baskets: typing.List[int]) -> int:
        n = len(fruits)
        size = 1
        while size < n:
            size <<= 1
        seg = [-1] * (2 * size)
        for i in range(n):
            seg[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            seg[i] = seg[2 * i] if seg[2 * i] > seg[2 * i + 1] else seg[2 * i + 1]
        def update(pos: int) -> None:
            idx = size + pos
            seg[idx] = -1
            idx //= 2
            while idx:
                left = seg[2 * idx]
                right = seg[2 * idx + 1]
                seg[idx] = left if left > right else right
                idx //= 2
        def query(fruit: int) -> int:
            if seg[1] < fruit:
                return -1
            idx = 1
            while idx < size:
                if seg[2 * idx] >= fruit:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - size
        unplaced = 0
        for f in fruits:
            pos = query(f)
            if pos == -1:
                unplaced += 1
            else:
                update(pos)
        return unplaced
