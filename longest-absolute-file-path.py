
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0
        level_lengths = { -1: 0 }

        for line in input.split('\n'):
            depth = line.rfind('\t') + 1
            name = line[depth:]

            parent_path_len = level_lengths[depth - 1]
            current_item_path_len = parent_path_len + len(name) + (1 if depth > 0 else 0)

            if '.' in name:
                max_length = max(max_length, current_item_path_len)
            else:
                level_lengths[depth] = current_item_path_len

        return max_length