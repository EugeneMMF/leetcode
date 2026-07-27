from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = [False] * n
        i = 0
        score = 0
        while 0 <= i < n and not visited[i]:
            visited[i] = True
            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i += values[i]
        return score
