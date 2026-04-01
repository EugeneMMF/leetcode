class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_valid_char_info(string_val, start_idx):
            backspace_count = 0
            current_idx = start_idx
            while current_idx >= 0:
                if string_val[current_idx] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return current_idx, string_val[current_idx]
                current_idx -= 1
            return -1, ''

        ptr_s = len(s) - 1
        ptr_t = len(t) - 1

        while ptr_s >= 0 or ptr_t >= 0:
            effective_idx_s, char_s = get_next_valid_char_info(s, ptr_s)
            effective_idx_t, char_t = get_next_valid_char_info(t, ptr_t)

            if char_s != char_t:
                return False
            
            ptr_s = effective_idx_s - 1
            ptr_t = effective_idx_t - 1
        
        return True

