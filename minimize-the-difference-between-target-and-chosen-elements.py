class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums = {0}
        for row in mat:
            new_sums = set()
            for val in row:
                for s in sums:
                    new_sums.add(s + val)
            sums = new_sums
        return min(abs(target - s) for s in sums)
