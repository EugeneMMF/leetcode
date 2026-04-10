class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        n = len(row) // 2
        pos = [0] * (2 * n)
        for i in range(2 * n):
            pos[row[i]] = i

        swaps = 0
        for i in range(0, 2 * n, 2):
            person1 = row[i]
            if person1 % 2 == 0:
                person2 = person1 + 1
            else:
                person2 = person1 - 1

            if row[i+1] != person2:
                swaps += 1
                person2_idx = pos[person2]
                
                pos[row[i+1]] = person2_idx
                pos[person2] = i + 1

                row[i+1], row[person2_idx] = row[person2_idx], row[i+1]
        return swaps
