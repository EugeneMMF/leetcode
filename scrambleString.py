class Solution:
  mapping = {}
  def isScramble(self, s1: str, s2: str) -> bool:
    if s1 == s2: return True
    if s1+s2 in self.mapping: return self.mapping[s1+s2]
    n = len(s1)
    f1, f2, f3 = ([0]*26 for _ in range(3))
    for i in range(1,n):
      j = n-i
      f1[ord(s1[i-1])-ord('a')]+=1
      f2[ord(s2[i-1])-ord('a')]+=1
      f3[ord(s2[j])-ord('a')]+=1
      if f1 == f2 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        self.mapping[s1+s2] = True
        return True
      if f1 == f3 and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
        self.mapping[s1+s2] = True
        return True
    self.mapping[s1+s2] = False
    return False

print(Solution().isScramble("abcdbdacbdac", "bdacabcdbdac"))