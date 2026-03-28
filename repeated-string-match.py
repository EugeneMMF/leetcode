class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)

        count = (len_b + len_a - 1) // len_a

        repeated_a = a * count

        if b in repeated_a:
            return count

        repeated_a += a
        if b in repeated_a:
            return count + 1
        
        repeated_a += a
        if b in repeated_a:
            return count + 2

        return -1
