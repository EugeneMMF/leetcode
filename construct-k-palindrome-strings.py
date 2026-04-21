class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        odd = sum(c & 1 for c in freq)
        return odd <= k
