class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1

            if i == n and j == n:
                return True
            if i == n or j == n:
                return False

            if start[i] != result[j]:
                return False

            if start[i] == 'L':
                if j > i:
                    return False
            elif start[i] == 'R':
                if j < i:
                    return False
            
            i += 1
            j += 1
        
        while i < n and start[i] == 'X':
            i += 1
        while j < n and result[j] == 'X':
            j += 1

        return i == n and j == n
