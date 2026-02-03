from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    wordDict = set(wordDict)
    solutions = []
    l = len(s)
    starts = [(0,0)]
    current = []
    while starts:
      start,end = starts.pop()
      if start != end: current.pop()
      i = end + 1
      while i <= l:
        if s[start:i] in wordDict:
          starts.append((start,i))
          starts.append((i,i))
          current.append(s[start:i])
          if i == l: solutions.append(" ".join(current))
          break
        i += 1
    return solutions

print(Solution().wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))