class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))

        mark = len(s) 
        
        for i in range(len(s) - 2, -1, -1):
            if s[i] > s[i+1]:
                s[i] = str(int(s[i]) - 1)
                mark = i + 1
        
        for i in range(mark, len(s)):
            s[i] = '9'
            
        return int("".join(s))
