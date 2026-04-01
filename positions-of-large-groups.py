class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        n = len(s)
        
        j = 0
        for i in range(n + 1):
            if i == n or s[i] != s[j]:
                group_length = i - j
                if group_length >= 3:
                    result.append([j, i - 1])
                j = i
        return result
