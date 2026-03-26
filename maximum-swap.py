class Solution:
    def maximumSwap(self, num: int) -> int:
        s_digits = list(str(num))
        n = len(s_digits)

        for i in range(n):
            max_val_in_suffix = -1
            max_idx_in_suffix = -1

            for k in range(n - 1, i, -1):
                if int(s_digits[k]) > max_val_in_suffix:
                    max_val_in_suffix = int(s_digits[k])
                    max_idx_in_suffix = k
            
            if max_idx_in_suffix != -1 and int(s_digits[i]) < max_val_in_suffix:
                s_digits[i], s_digits[max_idx_in_suffix] = s_digits[max_idx_in_suffix], s_digits[i]
                return int("".join(s_digits))
        
        return num
