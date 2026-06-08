class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        totalY = customers.count('Y')
        best_penalty = None
        best_j = 0
        prefixY = 0
        for j in range(n + 1):
            penalty = j + totalY - 2 * prefixY
            if best_penalty is None or penalty < best_penalty:
                best_penalty = penalty
                best_j = j
            if j < n and customers[j] == 'Y':
                prefixY += 1
        return best_j
