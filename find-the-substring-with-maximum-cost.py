class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = {c: v for c, v in zip(chars, vals)}
        max_ending = 0
        max_so_far = 0
        for ch in s:
            val = mapping.get(ch, ord(ch) - 96)
            max_ending = max(0, max_ending + val)
            if max_ending > max_so_far:
                max_so_far = max_ending
        return max_so_far
