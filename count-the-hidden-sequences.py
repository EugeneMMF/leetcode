class Solution:
    def numberOfArrays(self, differences, lower, upper):
        prefix = 0
        max_lower = lower
        min_upper = upper
        for d in differences:
            prefix += d
            max_lower = max(max_lower, lower - prefix)
            min_upper = min(min_upper, upper - prefix)
        return max(0, min_upper - max_lower + 1)
