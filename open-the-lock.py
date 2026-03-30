from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            current_combination, moves = queue.popleft()

            if current_combination == target:
                return moves

            for i in range(4):
                digit = int(current_combination[i])

                # Move forward
                next_digit_forward = str((digit + 1) % 10)
                next_combination_forward = list(current_combination)
                next_combination_forward[i] = next_digit_forward
                next_combination_forward = "".join(next_combination_forward)

                if next_combination_forward not in visited and next_combination_forward not in deadends_set:
                    visited.add(next_combination_forward)
                    queue.append((next_combination_forward, moves + 1))

                # Move backward
                next_digit_backward = str((digit - 1 + 10) % 10)
                next_combination_backward = list(current_combination)
                next_combination_backward[i] = next_digit_backward
                next_combination_backward = "".join(next_combination_backward)

                if next_combination_backward not in visited and next_combination_backward not in deadends_set:
                    visited.add(next_combination_backward)
                    queue.append((next_combination_backward, moves + 1))

        return -1
