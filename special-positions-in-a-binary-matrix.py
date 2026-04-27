class Solution:
    def numSpecial(self, mat):
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]
        count = 0
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count
