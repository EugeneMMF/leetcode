class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1:
            return 1
        accepted: dict[int, set[int]] = {i: set() for i in range(1, n+1)}
        for i in range(1, n+1):
            accepted[1].add(i)
            for j in range(i, n+1, i):
                if j % i == 0 or i % j == 0:
                    accepted[i].add(j)
                    accepted[j].add(i)
        def check(my_set: dict[int, set[int]], positions: set[int]) -> int:
            if len(positions) == 0:
                return 1
            if any(len(my_set[i]) == 0 for i in positions):
                return 0
            position_counts = {i: len(my_set[i]) for i in positions}
            value = sorted(position_counts.items(), key=lambda x: x[1])[0][0]
            positions.remove(value)
            count = 0
            for i in my_set[value]:
                to_readd = []
                for pos in positions:
                    if i in my_set[pos]:
                        my_set[pos].remove(i)
                        to_readd.append(pos)
                count += check(my_set, positions)
                for pos in to_readd:
                    my_set[pos].add(i)
            positions.add(value)
            return count
        return check(accepted, set(range(1, n+1)))