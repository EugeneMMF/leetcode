class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        for ch in t:
            cnt[ord(ch) - 97] -= 1
        steps = 0
        for c in cnt:
            steps += abs(c)
        return steps