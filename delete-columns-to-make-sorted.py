class Solution:
    def minDeletionSize(self, strs):
        if not strs:
            return 0
        m = len(strs)
        n = len(strs[0])
        deletions = 0
        for col in range(n):
            for row in range(1, m):
                if strs[row][col] < strs[row-1][col]:
                    deletions += 1
                    break
        return deletions
