from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        res = []
        while self.ptr <= self.n and self.arr[self.ptr] is not None:
            res.append(self.arr[self.ptr])
            self.ptr += 1
        return res
