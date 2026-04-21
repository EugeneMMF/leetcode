from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for j in range(n):
            left_smaller = left_greater = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1
            right_larger = right_smaller = 0
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                else:
                    right_smaller += 1
            total += left_smaller * right_larger + left_greater * right_smaller
        return total
