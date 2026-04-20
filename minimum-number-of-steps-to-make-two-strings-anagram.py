class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        steps = 0
        for ch in t:
            idx = ord(ch) - 97
            if freq[idx] > 0:
                freq[idx] -= 1
            else:
                steps += 1
        return steps
