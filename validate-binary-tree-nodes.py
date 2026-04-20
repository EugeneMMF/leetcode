class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        indeg = [0] * n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l != -1:
                indeg[l] += 1
                if indeg[l] > 1:
                    return False
            if r != -1:
                indeg[r] += 1
                if indeg[r] > 1:
                    return False
        roots = [i for i, d in enumerate(indeg) if d == 0]
        if len(roots) != 1:
            return False
        root = roots[0]
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            l = leftChild[node]
            r = rightChild[node]
            if l != -1:
                stack.append(l)
            if r != -1:
                stack.append(r)
        return len(visited) == n
