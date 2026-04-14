from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n <= 1:
            return 0
        m = len(strs[0])
        sorted_pair = [False] * (n - 1)
        deletions = 0
        for c in range(m):
            need_delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][c] > strs[i + 1][c]:
                    need_delete = True
                    break
            if need_delete:
                deletions += 1
                continue
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][c] < strs[i + 1][c]:
                    sorted_pair[i] = True
        return deletions
