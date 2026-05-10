class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        mapv = {'a':0,'e':1,'i':2,'o':3,'u':4}
        start = 0
        counts = [0]*5
        last = -1
        best = 0
        for i,ch in enumerate(word):
            idx = mapv[ch]
            if idx < last:
                start = i
                counts = [0]*5
                counts[idx] = 1
                last = idx
            else:
                counts[idx] += 1
                last = idx
                if all(c>0 for c in counts):
                    best = max(best, i-start+1)
        return best