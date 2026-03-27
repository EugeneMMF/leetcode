class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_count = 0
        current_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_count += 1
            else:
                ans += min(prev_count, current_count)
                prev_count = current_count
                current_count = 1
        
        ans += min(prev_count, current_count)
        
        return ans
