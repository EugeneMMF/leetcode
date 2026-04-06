class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        
        counts = defaultdict(int)
        
        for length in range(minSize, maxSize + 1):
            for i in range(len(s) - length + 1):
                substring = s[i:i+length]
                if len(set(substring)) <= maxLetters:
                    counts[substring] += 1
                    
        if not counts:
            return 0
            
        return max(counts.values())

