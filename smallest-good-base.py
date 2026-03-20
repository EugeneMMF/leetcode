import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)

        # The maximum possible value for m (the number of '1's in base k).
        # N = 1 + k + k^2 + ... + k^(m-1)
        # Since the smallest possible base k is 2, we have:
        # N >= 1 + 2 + 2^2 + ... + 2^(m-1) = 2^m - 1
        # From this, 2^m <= N + 1, which implies m <= log2(N + 1).
        # So, the largest integer m can be is floor(log2(N + 1)).
        # We iterate m downwards from this maximum value to 2.
        # This is because a larger 'm' corresponds to a smaller 'k' for a fixed 'N'.
        # Therefore, the first 'k' we find will be the smallest 'k' overall.
        
        # Example for max_m:
        # If N = 3, floor(log2(3+1)) = floor(log2(4)) = 2.
        # The loop will iterate for m = 2.
        # If N = 10^18, floor(log2(10^18+1)) = 59.
        # The loop will iterate for m from 59 down to 2.

        for m in range(math.floor(math.log2(N + 1)), 1, -1):
            # Binary search for k for the current fixed m.
            # The base k must be at least 2.
            low = 2
            
            # The upper bound for k can be derived from k^(m-1) < N, so k < N^(1/(m-1)).
            # We add 1 for safety to ensure the true k is included in the search range.
            # For m = 2, high becomes int(N**(1.0/1)) + 1 = N + 1.
            high = int(N**(1.0 / (m - 1))) + 1
            
            # If high is less than low, it means N^(1/(m-1)) is very small (e.g., < 2),
            # implying that even k=2 would make the sum too large for this m, or no k >= 2 exists.
            if high < low:
                continue

            k_found_for_m = -1

            while low <= high:
                mid = (low + high) // 2
                
                # Calculate the sum S = 1 + mid + mid^2 + ... + mid^(m-1)
                # We need to perform this calculation carefully to prevent integer overflow
                # and to efficiently determine if S equals N, is less than N, or greater than N.
                current_sum = 1
                power_k = 1
                is_valid_candidate = True

                for _ in range(1, m): # Loop m-1 times to reach mid^(m-1)
                    # Check for potential overflow: if power_k * mid would exceed N.
                    # We check N // mid < power_k instead of power_k * mid > N to prevent overflow
                    # if power_k * mid itself would exceed the integer limit before comparison.
                    if power_k > N // mid: 
                        is_valid_candidate = False
                        break
                    power_k *= mid
                    
                    # Check for potential overflow: if current_sum + power_k would exceed N.
                    # This also ensures current_sum doesn't exceed N prematurely.
                    if current_sum > N - power_k: 
                        is_valid_candidate = False
                        break
                    current_sum += power_k
                
                if is_valid_candidate:
                    if current_sum == N:
                        # Found a k that makes current_sum equal to N.
                        # Since we are looking for the smallest k for this specific m,
                        # we store it and try to find an even smaller k in the left half.
                        k_found_for_m = mid
                        high = mid - 1
                    elif current_sum < N:
                        # The sum is too small, so we need a larger base k.
                        low = mid + 1
                    else: # current_sum > N
                        # The sum is too large, so we need a smaller base k.
                        high = mid - 1
                else: 
                    # If is_valid_candidate is False (due to overflow or sum exceeding N),
                    # it means 'mid' is too large, so we try a smaller 'mid'.
                    high = mid - 1

            if k_found_for_m != -1:
                # If we found a k for the current m, it is the smallest good base
                # because we are iterating m downwards (larger m implies smaller k overall),
                # and the binary search finds the smallest k for this m.
                return str(k_found_for_m)
        
        # This part should theoretically be unreachable because m=2 (k=N-1) is always a solution
        # and would be found by the loop. However, as a safeguard or if problem constraints allowed,
        # N-1 is always a good base (N in base N-1 is "11").
        return str(N - 1)

