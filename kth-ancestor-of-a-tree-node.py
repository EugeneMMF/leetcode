from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.LOG = n.bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)]
        for i in range(n):
            self.up[i][0] = parent[i]
        for j in range(1, self.LOG):
            for i in range(n):
                p = self.up[i][j - 1]
                self.up[i][j] = self.up[p][j - 1] if p != -1 else -1

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k and node != -1:
            if k & 1:
                node = self.up[node][i]
            k >>= 1
            i += 1
        return node
