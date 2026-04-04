class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        
        def permutations(n_val, k_val):
            if k_val < 0 or k_val > n_val:
                return 0
            res = 1
            for i in range(k_val):
                res *= (n_val - i)
            return res

        s_n = str(n)
        length = len(s_n)
        count_no_repeated = 0

        for k in range(1, length):
            count_no_repeated += 9 * permutations(9, k - 1)

        digits = [int(d) for d in s_n]
        visited_mask = 0

        for idx in range(length):
            upper_bound_digit = digits[idx]
            start_loop_digit = 1 if idx == 0 else 0

            for d in range(start_loop_digit, upper_bound_digit):
                if (visited_mask >> d) & 1:
                    continue
                
                remaining_positions = length - 1 - idx
                
                num_used_total = bin(visited_mask | (1 << d)).count('1')
                
                available_choices = 10 - num_used_total 
                
                count_no_repeated += permutations(available_choices, remaining_positions)

            if (visited_mask >> upper_bound_digit) & 1:
                break
            
            visited_mask |= (1 << upper_bound_digit)
        else:
            count_no_repeated += 1

        return n - count_no_repeated
