from typing import List
from collections import deque
from string import ascii_lowercase

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    count = 1
    wordList = set(wordList)
    wordsUsed = set([beginWord])
    w = deque([beginWord])
    while w:
      s = len(w)
      for _ in range(s):
        word = w.popleft()
        word = list(word)
        for i,l in enumerate(word):
          pt = [*word]
          for j in ascii_lowercase:
            if l == j:
              continue
            pt[i] = j
            temp = "".join(pt)
            if temp in wordList:
              w.append(temp)
              wordList.remove(temp)
              if temp == endWord:
                return count+1
      count += 1
    return 0

print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))