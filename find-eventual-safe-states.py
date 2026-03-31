class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe = [None] * n

        def is_safe(node):
            if safe[node] is not None:
                return safe[node]

            safe[node] = False  # Mark as visiting

            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False

            safe[node] = True  # Mark as safe
            return True

        result = []
        for i in range(n):
            if is_safe(i):
                result.append(i)

        return result

