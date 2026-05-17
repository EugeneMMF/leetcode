from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        subtree = [0] * n
        stack = [(0, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                for child in children[node]:
                    stack.append((child, False))
            else:
                total = 1
                for child in children[node]:
                    total += subtree[child]
                subtree[node] = total
        max_score = 0
        count = 0
        for i in range(n):
            score = 1
            for child in children[i]:
                score *= subtree[child]
            if i != 0:
                score *= (n - subtree[i])
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1
        return count
