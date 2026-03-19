class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        # Max n-digit number (e.g., for n=2, 99)
        max_factor = 10**n - 1
        # Min n-digit number (e.g., for n=2, 10)
        min_factor = 10**(n - 1)

        # The largest possible palindrome will have 2n digits.
        # Its left half will be an n-digit number.
        # We iterate the 'left_half' of the palindrome downwards.
        # Starting from 'max_factor' ensures we find larger palindromes first.
        # For n > 1, any 2n-digit number is larger than any (2n-1)-digit number.
        # So we only need to consider 2n-digit palindromes.
        # The smallest possible left_half to form a 2n-digit palindrome
        # would be min_factor (e.g., 10 for n=2 forming 1001).
        for left_half in range(max_factor, min_factor - 1, -1):
            s_left_half = str(left_half)
            # Construct the 2n-digit palindrome
            palindrome_val = int(s_left_half + s_left_half[::-1])

            # Check if palindrome_val can be factored into two n-digit numbers (i * j)
            # Both i and j must be within [min_factor, max_factor].
            # We iterate i from max_factor downwards.
            # If palindrome_val = i * j, then j = palindrome_val / i.
            # Condition 1: j <= max_factor  =>  palindrome_val / i <= max_factor  =>  i >= palindrome_val / max_factor
            # Condition 2: j >= min_factor  =>  palindrome_val / i >= min_factor  =>  i <= palindrome_val / min_factor
            # So, i must be in the range [max(min_factor, palindrome_val // max_factor), max_factor].
            
            # The inner loop iterates i downwards.
            # It starts from max_factor and goes down to palindrome_val // max_factor (inclusive).
            # The `range` function's stop argument is exclusive, so we use -1.
            for i in range(max_factor, palindrome_val // max_factor - 1, -1):
                # Optimization: if i becomes less than min_factor,
                # then i is no longer an n-digit number, so we can break early.
                if i < min_factor:
                    break
                
                # Check if i is a factor of palindrome_val
                if palindrome_val % i == 0:
                    j = palindrome_val // i
                    # Check if j is also an n-digit number.
                    # The upper bound for j (j <= max_factor) is implicitly covered
                    # by the inner loop's lower bound for i (i >= palindrome_val // max_factor).
                    # We only need to explicitly check if j meets its lower bound.
                    if j >= min_factor:
                        return palindrome_val % 1337
        
        # This part should theoretically not be reached given the problem constraints (1 <= n <= 8)
        # and the guarantee that a solution exists.
        return -1

