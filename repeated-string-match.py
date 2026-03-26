class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        num_repeats = (len_b + len_a - 1) // len_a
        s_repeated = a * num_repeats
        if b in s_repeated:
            return num_repeats
        s_repeated_plus_one = a * (num_repeats + 1)
        if b in s_repeated_plus_one:
            return num_repeats + 1
        return -1
