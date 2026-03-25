class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def find_shortest_prefix(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end_of_word:
                return node.word
        return word

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(" ")
        result = []
        for word in words:
            result.append(trie.find_shortest_prefix(word))

        return " ".join(result)

