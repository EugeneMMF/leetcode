class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        arr = list(s)
        moves = 0
        i = 0
        while i < n:
            if arr[i] == 'X':
                moves += 1
                for j in range(i, min(i + 3, n)):
                    arr[j] = 'O'
                i += 3
            else:
                i += 1
        return moves
