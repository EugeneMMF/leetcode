class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class Node:
            __slots__ = ("children", "best")
            def __init__(self):
                self.children = {}
                self.best = None
        root = Node()
        for idx, w in enumerate(wordsContainer):
            node = root
            l = len(w)
            if node.best is None or l < node.best[0] or (l == node.best[0] and idx < node.best[1]):
                node.best = (l, idx)
            for ch in reversed(w):
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                if node.best is None or l < node.best[0] or (l == node.best[0] and idx < node.best[1]):
                    node.best = (l, idx)
        ans = []
        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break
            ans.append(node.best[1])
        return ans
