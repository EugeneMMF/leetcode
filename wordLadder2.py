from typing import List
from collections import deque
from string import ascii_lowercase

class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    depths = {beginWord: 1}
    solution = []
    wordSet = set(wordList)
    words = deque([beginWord])
    if beginWord in wordSet: wordSet.remove(beginWord)

    def dfs(word, sequence):
      if word == beginWord:
        solution.append(list(reversed(sequence)))
        return
      depth = depths[word]
      tmpWord = list(word)
      for i,letter in enumerate(word):
        for substitute in ascii_lowercase:
          tmpWord[i] = substitute
          newWord = "".join(tmpWord)
          if newWord in depths and depths[newWord] + 1 == depth:
            sequence.append(newWord)
            dfs(newWord, sequence)
            sequence.pop()
        tmpWord[i] = letter

    depth = 1
    while words:
      word = words.popleft()
      if word == endWord:
        break
      depth = depths[word]
      word = list(word)
      tmpWord = [*word]
      for i,letter in enumerate(word):
        for substitute in ascii_lowercase:
          tmpWord[i] = substitute
          newWord = "".join(tmpWord)
          if newWord in wordSet:
            words.append(newWord)
            wordSet.remove(newWord)
            depths[newWord] = depth + 1
        tmpWord[i] = letter
    if endWord in depths:
      dfs(endWord, [endWord])
    return solution