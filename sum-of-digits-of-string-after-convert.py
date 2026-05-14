class Solution:
    def getLucky(self, s: str, k: int) -> int:
        concat = ''.join(str(ord(c) - 96) for c in s)
        total = sum(int(ch) for ch in concat)
        for _ in range(k - 1):
            total = sum(int(d) for d in str(total))
        return total
