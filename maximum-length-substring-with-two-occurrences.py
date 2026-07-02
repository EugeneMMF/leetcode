class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            while counts[ch] > 2:
                left_ch = s[left]
                counts[left_ch] -= 1
                if counts[left_ch] == 0:
                    del counts[left_ch]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
