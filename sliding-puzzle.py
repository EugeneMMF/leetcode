
import collections

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        target = "123450"
        initial_state = "".join(str(num) for row in board for num in row)
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        queue = collections.deque([(initial_state, 0)])
        visited = {initial_state}
        while queue:
            current_board_string, moves = queue.popleft()
            if current_board_string == target:
                return moves
            zero_idx = current_board_string.find('0')
            for next_zero_idx in adj[zero_idx]:
                next_board_list = list(current_board_string)
                next_board_list[zero_idx], next_board_list[next_zero_idx] = \
                    next_board_list[next_zero_idx], next_board_list[zero_idx]
                next_board_string = "".join(next_board_list)
                if next_board_string not in visited:
                    visited.add(next_board_string)
                    queue.append((next_board_string, moves + 1))
        return -1

