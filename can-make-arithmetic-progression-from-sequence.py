class Solution:
    def canMakeArithmeticProgression(self, arr):
        n = len(arr)
        if n <= 2:
            return True
        mn = min(arr)
        mx = max(arr)
        diff_num = mx - mn
        if diff_num % (n - 1) != 0:
            return False
        d = diff_num // (n - 1)
        if d == 0:
            return all(x == mn for x in arr)
        seen = set(arr)
        for i in range(n):
            if mn + i * d not in seen:
                return False
        return True
