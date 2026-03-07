class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # For n=1, numbers are 0-9. All have unique digits. Count is 10.
        total_count = 10
        
        # 'current_product' calculates the number of unique-digit numbers for a specific length.
        # For 2-digit numbers: the first digit has 9 choices (1-9).
        current_product = 9 
        
        # Iterate for numbers with 2 digits up to n digits (or 10 digits max, as no more than 10 unique digits exist).
        for k in range(2, min(n, 10) + 1):
            # For the k-th digit, there are (11 - k) choices left, as k-1 digits are already used.
            # Example:
            # k=2: 9 * (10 - 1) = 9 * 9 = 81 (for 2-digit numbers with unique digits)
            # k=3: 81 * (10 - 2) = 81 * 8 = 648 (for 3-digit numbers with unique digits)
            current_product *= (11 - k)
            total_count += current_product
            
        return total_count
