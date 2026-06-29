class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        prefV = [0]*(n+1)
        vowels = set('aeiou')
        for i,ch in enumerate(s,1):
            prefV[i] = prefV[i-1] + (1 if ch in vowels else 0)
        # compute L
        ktemp = k
        L = 1
        p = 2
        while p*p <= ktemp:
            if ktemp%p==0:
                e = 0
                while ktemp%p==0:
                    ktemp//=p
                    e+=1
                exp = (e+1)//2
                L*=p**exp
            p+=1
        if ktemp>1:
            L*=ktemp**1
        # group by d = 2*prefV - i
        groups = {}
        for i in range(n+1):
            d = 2*prefV[i] - i
            mod = prefV[i] % L if L!=0 else 0
            if d not in groups:
                groups[d] = {}
            sub = groups[d]
            sub[mod] = sub.get(mod,0)+1
        ans = 0
        for sub in groups.values():
            for cnt in sub.values():
                ans += cnt*(cnt-1)//2
        return ans
