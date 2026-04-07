class Solution:
    def sortString(self, s: str) -> str:
        counts = [0] * 26
        for char_code in map(ord, s):
            counts[char_code - ord('a')] += 1
        
        result = []
        n = len(s)

        while len(result) < n:
            # Phase 1: Smallest -> Increasing
            for i in range(26):
                if counts[i] > 0:
                    result.append(chr(ord('a') + i))
                    counts[i] -= 1
            
            # Phase 2: Largest -> Decreasing
            for i in range(25, -1, -1):
                if counts[i] > 0:
                    result.append(chr(ord('a') + i))
                    counts[i] -= 1
        
        return "".join(result)
