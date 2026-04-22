from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        table_counts = defaultdict(lambda: defaultdict(int))
        for _, table, food in orders:
            foods.add(food)
            table_counts[table][food] += 1
        food_list = sorted(foods)
        result = [["Table"] + food_list]
        for table in sorted(table_counts, key=int):
            row = [table]
            cnt = table_counts[table]
            for f in food_list:
                row.append(str(cnt.get(f, 0)))
            result.append(row)
        return result
