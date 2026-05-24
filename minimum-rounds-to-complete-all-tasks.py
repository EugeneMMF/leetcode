class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        freq = Counter(tasks)
        total = 0
        for c in freq.values():
            if c == 1:
                return -1
            if c % 3 == 0:
                total += c // 3
            elif c % 3 == 1:
                total += c // 3 + 1
            else:  # c % 3 == 2
                total += c // 3 + 1
        return total
