class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_parts = []
            for i in range(0, len(s), k):
                group = s[i:i+k]
                sum_digits = sum(int(c) for c in group)
                new_parts.append(str(sum_digits))
            s = "".join(new_parts)
        return s
