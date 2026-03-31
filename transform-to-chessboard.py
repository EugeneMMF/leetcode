class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)

        def calculate_min_swaps_1d(arr_1d, length):
            swaps_target_0 = 0
            swaps_target_1 = 0
            
            count_zeros = 0
            for i in range(length):
                if arr_1d[i] == 0:
                    count_zeros += 1
                
                if arr_1d[i] != (i % 2):
                    swaps_target_0 += 1
                
                if arr_1d[i] != ((i + 1) % 2):
                    swaps_target_1 += 1
            
            count_ones = length - count_zeros

            if length % 2 == 0:
                if count_zeros != length // 2 or count_ones != length // 2:
                    return float('inf')
            else:
                if not (abs(count_zeros - count_ones) == 1):
                    return float('inf')
            
            res = float('inf')

            if length % 2 == 0:
                if swaps_target_0 % 2 == 0:
                    res = min(res, swaps_target_0 // 2)
                if swaps_target_1 % 2 == 0:
                    res = min(res, swaps_target_1 // 2)
            else:
                if count_zeros == (length + 1) // 2:
                    if swaps_target_0 % 2 == 0:
                        res = min(res, swaps_target_0 // 2)
                elif count_ones == (length + 1) // 2:
                    if swaps_target_1 % 2 == 0:
                        res = min(res, swaps_target_1 // 2)
            
            return res

        for i in range(n):
            for j in range(n):
                if board[i][j] != (board[i][0] ^ board[0][j] ^ board[0][0]):
                    return -1
        
        row_first_elements = [board[i][0] for i in range(n)]
        col_first_elements = [board[0][j] for j in range(n)]

        ans_rows = calculate_min_swaps_1d(row_first_elements, n)
        ans_cols = calculate_min_swaps_1d(col_first_elements, n)

        if ans_rows == float('inf') or ans_cols == float('inf'):
            return -1
        
        return ans_rows + ans_cols

