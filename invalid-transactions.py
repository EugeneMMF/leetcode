from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))
        invalid = [False] * n
        for i in range(n):
            name_i, time_i, amount_i, city_i = parsed[i]
            if amount_i > 1000:
                invalid[i] = True
            for j in range(i + 1, n):
                name_j, time_j, amount_j, city_j = parsed[j]
                if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                    invalid[i] = True
                    invalid[j] = True
        return [transactions[i] for i in range(n) if invalid[i]]
