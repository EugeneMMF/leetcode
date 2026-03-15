class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = [0] * 26  # Frequency map for characters 'A' through 'Z'
        max_freq = 0      # Stores the maximum frequency of any character encountered in the current window
        max_length = 0    # Stores the maximum length found so far

        for right in range(len(s)):
            char_idx = ord(s[right]) - ord('A')
            counts[char_idx] += 1
            
            # max_freq is the maximum count of a single distinct character in the current window
            # It does not decrease when 'left' pointer moves, which is key to the O(N) solution.
            max_freq = max(max_freq, counts[char_idx])

            current_window_length = right - left + 1

            # If the number of characters to change (current_window_length - max_freq)
            # exceeds k, then the current window is invalid.
            # We must shrink the window from the left.
            if current_window_length - max_freq > k:
                # Remove the character at the left pointer from the window's counts
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            # After ensuring the window is valid (either it was already valid or
            # it became valid after shrinking), update max_length.
            # This captures the longest valid window found so far.
            max_length = max(max_length, right - left + 1)
            
        return max_length

