class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        freq = {}
        for row in matrix:
            if row[0] == 1:
                key = tuple(1 - x for x in row)
            else:
                key = tuple(row)
            freq[key] = freq.get(key, 0) + 1
        return max(freq.values()) if freq else 0
