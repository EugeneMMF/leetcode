from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)
    added = set()
    l = len(s)
    ll = l - 1
    starts = [(0,0)]
    while starts:
      start,end = starts.pop()
      i = end+1
      while i <= l:
        if s[start:i] in wordDict:
          if (start,i) not in added:
            starts.append((start,i))
            added.add((start,i))
            starts.append((i,i))
          if i == l: return True
          break
        i += 1
    return False

print(Solution().wordBreak("catsandog",["cats","dog","sand","and","cat"]))