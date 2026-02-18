import re

class WordDictionary:

  def __init__(self):
    self.root = {}

  def addWord(self, word: str) -> None:
    node = self.root
    for c in word:
      node[c] = node.get(c, {})
      node = node[c]
    node['_'] = True

  def search(self, word: str) -> bool:
    nodes = [(0, self.root)]
    word = list(word)
    while nodes:
      i, node = nodes.pop()
      while i < len(word):
        if word[i] == '.':
          for n in node.values():
            if not isinstance(n, bool): nodes.append((i+1, n))
          break
        elif nd:=node.get(word[i], None):
          node = nd
        else: break
        i += 1
      if i == len(word) and "_" in node: return True
    return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("word")
obj.addWord("ward")
obj.addWord("ab")
param_2 = obj.search("w.rd")
print(param_2)