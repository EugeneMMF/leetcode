import collections

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        counts = collections.Counter(s)

        excess_map = {}
        for char_key in ['Q', 'W', 'E', 'R']:
            excess_map[char_key] = max(0, counts[char_key] - target)

        if sum(excess_map.values()) == 0:
            return 0

        min_len = n
        left = 0
        window_counts = collections.Counter()

        satisfied_char_types = 0
        for char_key in ['Q', 'W', 'E', 'R']:
            if excess_map[char_key] == 0:
                satisfied_char_types += 1

        for right in range(n):
            char_r = s[right]
            window_counts[char_r] += 1

            if excess_map[char_r] > 0 and window_counts[char_r] == excess_map[char_r]:
                satisfied_char_types += 1
            
            while satisfied_char_types == 4:
                min_len = min(min_len, right - left + 1)

                char_l = s[left]
                
                if excess_map[char_l] > 0 and window_counts[char_l] == excess_map[char_l]:
                    satisfied_char_types -= 1
                
                window_counts[char_l] -= 1
                left += 1
        
        return min_len
