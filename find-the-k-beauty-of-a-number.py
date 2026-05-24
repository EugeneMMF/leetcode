class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        count = 0
        for i in range(n - k + 1):
            sub = s[i:i + k]
            val = int(sub)
            if val != 0 and num % val == 0:
                count += 1
        return count
