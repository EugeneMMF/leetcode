from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(comp) for comp in favoriteCompanies]
        n = len(sets)
        is_subset = [False] * n
        for i in range(n):
            if is_subset[i]:
                continue
            for j in range(n):
                if i == j:
                    continue
                if sets[i] <= sets[j]:
                    is_subset[i] = True
                    break
        return [i for i in range(n) if not is_subset[i]]
