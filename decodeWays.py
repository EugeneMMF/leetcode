class Solution:
  def numDecodings(self, s: str) -> int:
    s = list(s)
    if s[0] == "0":
      return 0
    ls = len(s)
    counts = [0]*ls + [1]
    if s[ls-1] != "0":
      counts[ls-1] = 1
    for i in range(ls-2, -1, -1):
      if s[i] != "0":
        counts[i] += counts[i+1]
        if s[i] < "3":
          if s[i] < "2" or s[i+1] < "7":
            counts[i] += counts[i+2]
    return counts[0]