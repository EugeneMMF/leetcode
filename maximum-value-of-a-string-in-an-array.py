class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            if s.isdigit():
                val = int(s)
            else:
                val = len(s)
            if val > max_val:
                max_val = val
        return max_val
