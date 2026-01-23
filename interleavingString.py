class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    def helperFunction(i, j):
      if i == l1 and j == l2: return True
      k = i + j
      if found[i][j] != None: return found[i][j]
      works = False
      if i < l1 and s1[i] == s3[k]:
        works |= helperFunction(i+1, j)
      if j < l2 and s2[j] == s3[k]:
        works |= helperFunction(i, j+1)
      found[i][j] = works
      return works

    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if l1 + l2 != l3: return False
    found = [[None]*(l2+1) for _ in range(l1+1)]
    return helperFunction(0, 0)