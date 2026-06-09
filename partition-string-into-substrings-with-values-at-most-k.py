class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        num = 0
        for ch in s:
            digit = ord(ch) - 48
            num = num * 10 + digit
            if num > k:
                count += 1
                num = digit
                if num > k:
                    return -1
        if num > 0:
            count += 1
        return count