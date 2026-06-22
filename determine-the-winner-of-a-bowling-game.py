class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(arr):
            n = len(arr)
            total = 0
            for i in range(n):
                if (i >= 1 and arr[i-1] == 10) or (i >= 2 and arr[i-2] == 10):
                    total += 2 * arr[i]
                else:
                    total += arr[i]
            return total
        s1, s2 = score(player1), score(player2)
        if s1 > s2:
            return 1
        if s2 > s1:
            return 2
        return 0
