class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Iterate to find the first number (num1)
        # num1_str = num[0:i]
        # Length of num1_str can range from 1 up to n - 2
        # (leaving at least 1 digit for num2 and 1 for the sum/third number)
        for i in range(1, n):
            num1_str = num[0:i]
            # Check for leading zeros: '01' is invalid, but '0' is valid.
            if len(num1_str) > 1 and num1_str[0] == '0':
                break # If num1 starts with '0' and has more than one digit, no further num1_str starting with '0' will be valid.

            # Iterate to find the second number (num2)
            # num2_str = num[i:j]
            # Length of num2_str can range from 1 up to n - i - 1
            # (leaving at least 1 digit for the sum/third number)
            for j in range(i + 1, n):
                num2_str = num[i:j]
                # Check for leading zeros for num2
                if len(num2_str) > 1 and num2_str[0] == '0':
                    break # Same logic as for num1

                num1 = int(num1_str)
                num2 = int(num2_str)

                # Now that num1 and num2 are chosen, start checking the additive sequence.
                # The remaining part of the string is num[j:].
                # We start with k=2 because num1 and num2 are already chosen numbers.
                if self._check(num1, num2, num[j:], 2):
                    return True
        return False

    # Recursive helper function to verify the additive sequence.
    # num1: the first preceding number in the current pair
    # num2: the second preceding number in the current pair
    # remaining_str: the part of the original string that needs to be consumed
    # k: the count of numbers already confirmed in the sequence (num1, num2, ..., previous_sum)
    def _check(self, num1: int, num2: int, remaining_str: str, k: int) -> bool:
        # Base case: If all digits in remaining_str have been consumed.
        # This means a potential additive sequence has been found.
        # We must ensure that at least three numbers were formed in total.
        if not remaining_str:
            return k >= 3

        # Calculate the sum of the two preceding numbers.
        s = str(num1 + num2)

        # Check if the sum (as a string) is a prefix of the remaining_str.
        # Also, the sum cannot be longer than the remaining_str itself.
        if len(s) > len(remaining_str) or not remaining_str.startswith(s):
            return False

        # If it matches, continue the sequence:
        # The new first preceding number becomes num2.
        # The new second preceding number becomes the current sum (num1 + num2).
        # The remaining string is shortened by the length of the matched sum.
        # Increment k as we've successfully found one more number in the sequence.
        return self._check(num2, num1 + num2, remaining_str[len(s):], k + 1)
