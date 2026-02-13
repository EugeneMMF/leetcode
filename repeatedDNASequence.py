from typing import List

class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    l = len(s)
    if l <= 10: return []
    counts = set()
    result = set()
    for i in range(l-9):
      if s[i:i+10] in counts:
        result.add(s[i:i+10])
      else:
        counts.add(s[i:i+10])
    return list(result)