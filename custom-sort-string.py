import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = collections.Counter(s)
        
        result_chars = []
        for char_in_order in order:
            if char_in_order in s_counts:
                result_chars.append(char_in_order * s_counts[char_in_order])
                s_counts[char_in_order] = 0
        
        for char_remaining, count_remaining in s_counts.items():
            if count_remaining > 0:
                result_chars.append(char_remaining * count_remaining)
        
        return "".join(result_chars)
