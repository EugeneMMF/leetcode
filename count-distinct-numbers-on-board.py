class Solution:
    def distinctIntegers(self, n: int) -> int:
        board = {n}
        changed = True
        while changed:
            changed = False
            new_set = set(board)
            for x in board:
                for i in range(1, n + 1):
                    if x % i == 1 and i not in board:
                        new_set.add(i)
                        changed = True
            board = new_set
        return len(board)