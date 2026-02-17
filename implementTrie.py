class Trie:

  def __init__(self):
    self.root = {}

  def insert(self, word: str) -> None:
    node = self.root
    for char in word:
      node[char] = node.get(char, {})
      node = node[char]
    node['_'] = True

  def search(self, word: str) -> bool:
    node = self.root
    for char in word:
      if char not in node:
        return False
      node = node[char]
    return '_' in node

  def startsWith(self, prefix: str) -> bool:
    node = self.root
    for char in prefix:
      if char not in node:
        return False
      node = node[char]
    return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)