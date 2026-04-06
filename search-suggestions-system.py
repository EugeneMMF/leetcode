class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        root = TrieNode()

        for product in products:
            curr = root
            for char in product:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)
        
        result = []
        curr = root
        prefix_found = True

        for char in searchWord:
            if prefix_found:
                if char in curr.children:
                    curr = curr.children[char]
                    result.append(curr.suggestions)
                else:
                    prefix_found = False
                    result.append([])
            else:
                result.append([])
        
        return result
