class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = [10**9] * 26
        last_lower = [-1] * 26
        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                idx = ord(ch) - 97
                last_lower[idx] = i
            else:
                idx = ord(ch) - 65
                if i < first_upper[idx]:
                    first_upper[idx] = i
        count = 0
        for idx in range(26):
            if last_lower[idx] != -1 and first_upper[idx] != 10**9 and last_lower[idx] < first_upper[idx]:
                count += 1
        return count
