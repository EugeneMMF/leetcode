class Solution:
    def minSwaps(self, s: str) -> int:
        bal = 0
        max_neg = 0
        for ch in s:
            if ch == '[':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                max_neg += 1
                bal = 0
        return (max_neg + 1) // 2
