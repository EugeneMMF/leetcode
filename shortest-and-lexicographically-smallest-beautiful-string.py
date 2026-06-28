class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        prefix = [0]*(n+1)
        for i,ch in enumerate(s,1):
            prefix[i] = prefix[i-1] + (ch=='1')
        min_len = n+1
        for i in range(n):
            count = 0
            for j in range(i,n):
                if s[j]=='1':
                    count+=1
                if count==k:
                    length = j-i+1
                    if length<min_len:
                        min_len=length
                    break
        if min_len==n+1:
            return ""
        best = None
        for i in range(n-min_len+1):
            if prefix[i+min_len]-prefix[i]==k:
                sub = s[i:i+min_len]
                if best is None or sub<best:
                    best=sub
        return best