class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        new_parent = parent[:]
        from collections import defaultdict
        char_stack = defaultdict(list)
        stack = [(0, 0)]
        while stack:
            u, state = stack.pop()
            if state == 0:
                ch = s[u]
                if u != 0:
                    if char_stack[ch]:
                        new_parent[u] = char_stack[ch][-1]
                stack.append((u, 1))
                for v in reversed(children[u]):
                    stack.append((v, 0))
                char_stack[ch].append(u)
            else:
                char_stack[s[u]].pop()
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        sizes = [0] * n
        stack = [(0, 0)]
        while stack:
            u, state = stack.pop()
            if state == 0:
                stack.append((u, 1))
                for v in new_children[u]:
                    stack.append((v, 0))
            else:
                total = 1
                for v in new_children[u]:
                    total += sizes[v]
                sizes[u] = total
        return sizes
