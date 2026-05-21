class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1 = ord(s[0]) - 64
        row1 = int(s[1])
        col2 = ord(s[3]) - 64
        row2 = int(s[4])
        result = []
        for c in range(col1, col2 + 1):
            for r in range(row1, row2 + 1):
                result.append(chr(64 + c) + str(r))
        return result