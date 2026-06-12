class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_count = sum(mat[0])
        for i in range(1, len(mat)):
            count = sum(mat[i])
            if count > max_count:
                max_count = count
                max_row = i
        return [max_row, max_count]
