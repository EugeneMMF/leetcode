class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix_mask = [0]*n
        mask = 0
        for i in range(n):
            prefix_mask[i] = mask
            mask |= 1 << (ord(s[i]) - 97)
        suffix_mask = [0]*n
        mask = 0
        for i in range(n-1, -1, -1):
            suffix_mask[i] = mask
            mask |= 1 << (ord(s[i]) - 97)
        seen = set()
        for i in range(n):
            b = ord(s[i]) - 97
            before = prefix_mask[i]
            after = suffix_mask[i]
            common = before & after
            while common:
                c = (common & -common).bit_length() - 1
                seen.add(26*c + b)
                common &= common - 1
        return len(seen)
