class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0]) if m else 0
        shift = k % n if n else 0
        for i in range(m):
            row = mat[i]
            if shift == 0:
                continue
            if i % 2 == 0:
                new_row = row[shift:] + row[:shift]
            else:
                new_row = row[-shift:] + row[:-shift]
            if new_row != row:
                return False
        return True
