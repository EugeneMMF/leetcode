class Solution:
    def kthLargestValue(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        pref = [[0]*n for _ in range(m)]
        vals = []
        for i in range(m):
            row_xor = 0
            for j in range(n):
                a = matrix[i][j]
                if i > 0:
                    a ^= pref[i-1][j]
                if j > 0:
                    a ^= pref[i][j-1]
                if i > 0 and j > 0:
                    a ^= pref[i-1][j-1]
                pref[i][j] = a
                vals.append(a)
        import heapq
        return heapq.nlargest(k, vals)[-1]
