class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_needed = mean * (n + m)
        current_sum = sum(rolls)
        remaining = total_needed - current_sum
        if remaining < n or remaining > 6 * n:
            return []
        res = [1] * n
        extra = remaining - n
        for i in range(n):
            add = 5 if extra >= 5 else extra
            res[i] += add
            extra -= add
            if extra == 0:
                break
        return res
