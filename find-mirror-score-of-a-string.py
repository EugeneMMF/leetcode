class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = [25 - i for i in range(26)]
        stacks = [[] for _ in range(26)]
        score = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            m = mirror[idx]
            if stacks[m]:
                j = stacks[m].pop()
                score += i - j
            else:
                stacks[idx].append(i)
        return score