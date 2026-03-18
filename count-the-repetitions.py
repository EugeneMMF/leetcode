class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len_s1 = len(s1)
        len_s2 = len(s2)

        s1_chars = set(s1)
        if any(c not in s1_chars for c in s2):
            return 0

        match_result = [None] * len_s2

        for j in range(len_s2):
            current_s2_idx = j
            current_s2_blocks = 0
            for char_s1 in s1:
                if char_s1 == s2[current_s2_idx]:
                    current_s2_idx += 1
                    if current_s2_idx == len_s2:
                        current_s2_blocks += 1
                        current_s2_idx = 0
            match_result[j] = (current_s2_blocks, current_s2_idx)

        total_s2_blocks_matched = 0
        current_s2_idx = 0
        s1_blocks_consumed = 0

        history = {}

        while s1_blocks_consumed < n1:
            if current_s2_idx in history:
                prev_s1_blocks, prev_total_s2_blocks = history[current_s2_idx]
                
                cycle_len_s1 = s1_blocks_consumed - prev_s1_blocks
                cycle_len_s2 = total_s2_blocks_matched - prev_total_s2_blocks

                remaining_s1_blocks = n1 - s1_blocks_consumed
                num_cycles_to_jump = remaining_s1_blocks // cycle_len_s1

                total_s2_blocks_matched += num_cycles_to_jump * cycle_len_s2
                s1_blocks_consumed += num_cycles_to_jump * cycle_len_s1
                
            if s1_blocks_consumed < n1:
                history[current_s2_idx] = (s1_blocks_consumed, total_s2_blocks_matched)
                
                s2_blocks_in_current_s1, next_s2_idx = match_result[current_s2_idx]
                total_s2_blocks_matched += s2_blocks_in_current_s1
                current_s2_idx = next_s2_idx
                s1_blocks_consumed += 1
            else:
                break
        
        return total_s2_blocks_matched // n2
