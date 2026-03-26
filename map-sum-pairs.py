class TrieNode:
    def __init__(self):
        self.children = {}
        self.current_sum = 0

class MapSum:
    def __init__(self):
        self.trie = TrieNode()
        self.keys_map = {}

    def insert(self, key: str, val: int) -> None:
        old_val = self.keys_map.get(key, 0)
        delta_val = val - old_val
        
        self.keys_map[key] = val

        curr = self.trie
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.current_sum += delta_val

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        
        return curr.current_sum
