class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        max_length_for_binary_strings = 0
        if n >= 1:
            # Calculate the maximum length a binary representation of an integer up to 'n' can have.
            # bin(n) returns a string like '0b101', so we subtract 2 for the actual binary string length.
            max_length_for_binary_strings = len(bin(n)) - 2

        # The actual maximum length of a substring we need to extract from 's' is limited by two factors:
        # 1. The length of 's' itself.
        # 2. The maximum length of a binary string we care about (max_length_for_binary_strings).
        # This effective maximum length will be at most around 30 for n up to 10^9.
        effective_substring_max_len = min(len(s), max_length_for_binary_strings)

        found_values = set()

        # Iterate through all possible starting positions in 's'.
        for i in range(len(s)):
            # Iterate through possible lengths for substrings.
            # We only need to consider lengths up to effective_substring_max_len.
            for j in range(1, effective_substring_max_len + 1):
                # Ensure the substring does not go out of bounds.
                if i + j > len(s):
                    break
                
                substring = s[i : i+j]

                # Standard binary representations of positive integers do not have leading zeros,
                # unless the number itself is 0 (which is not in the range [1, n]).
                # So, skip substrings like "01", "001", etc. which are not standard binary forms for positive integers.
                if substring[0] == '0' and j > 1:
                    continue
                
                # Convert the binary substring to an integer.
                value = int(substring, 2)

                # Add the value to our set if it falls within the required range [1, n].
                # This also acts as an optimization to not store excessively large numbers
                # that are beyond what 'n' requires.
                if 1 <= value <= n:
                    found_values.add(value)

        # After generating all relevant binary values from substrings,
        # we check if all integers from 1 to n are present in our 'found_values' set.
        # Although 'n' can be up to 10^9, in cases where the answer is 'True',
        # 'n' must be relatively small because the maximum number of distinct binary values
        # that can be formed from substrings of 's' (with length up to ~30) is limited.
        # For len(s)=1000 and max_binary_length=30, this limit is approximately 30,000 values.
        # If 'n' is larger than this approximate limit, it's impossible for 'found_values' to contain
        # all numbers from 1 to 'n', and the loop will quickly find a missing number and return False.
        for k in range(1, n + 1):
            if k not in found_values:
                return False
        
        return True

