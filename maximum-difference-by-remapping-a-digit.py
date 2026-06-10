class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        min_val = 10**18
        max_val = -1
        for d1 in '0123456789':
            for d2 in '0123456789':
                new_s = s.replace(d1, d2)
                val = int(new_s)
                if val < min_val:
                    min_val = val
                if val > max_val:
                    max_val = val
        return max_val - min_val
