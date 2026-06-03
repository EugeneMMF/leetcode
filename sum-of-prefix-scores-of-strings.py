class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class Node:
            __slots__ = ('children', 'cnt')
            def __init__(self):
                self.children = {}
                self.cnt = 0
        root = Node()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                node.cnt += 1
        res = []
        for w in words:
            node = root
            total = 0
            for ch in w:
                node = node.children[ch]
                total += node.cnt
            res.append(total)
        return res
