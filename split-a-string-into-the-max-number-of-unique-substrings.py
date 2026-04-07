class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_splits = 0
        
        def backtrack(index, current_split):
            if index == len(s):
                self.max_splits = max(self.max_splits, len(current_split))
                return
            
            for i in range(index, len(s)):
                substring = s[index:i+1]
                if substring not in current_split:
                    current_split.add(substring)
                    backtrack(i + 1, current_split)
                    current_split.remove(substring)
                    
        backtrack(0, set())
        return self.max_splits
