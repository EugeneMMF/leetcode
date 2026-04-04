class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class StreamChecker:

    def __init__(self, words: list[str]):
        self.root = TrieNode()
        self.stream = ""
        for word in words:
            node = self.root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        node = self.root
        for i in range(len(self.stream) - 1, -1, -1):
            char = self.stream[i]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end_of_word:
                return True
        return False
