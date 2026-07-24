class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        while True:
            removal = 10 - turn
            if removal <= 0:
                return False
            if n < removal:
                return turn % 2 == 1
            n -= removal
            turn += 1