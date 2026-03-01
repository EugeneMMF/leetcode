from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        # Build adjacency list and calculate degrees
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initialize leaves queue: add all nodes with degree 1
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        # Iteratively remove leaves layer by layer
        remaining_nodes = n
        while remaining_nodes > 2:
            # Get the number of leaves in the current layer
            num_leaves_in_current_level = len(leaves)
            # Reduce the total count of nodes by the number of leaves removed
            remaining_nodes -= num_leaves_in_current_level

            # Process all leaves in the current layer
            for _ in range(num_leaves_in_current_level):
                u = leaves.popleft()
                # For each neighbor of the removed leaf 'u'
                for v in adj[u]:
                    # Decrement the degree of the neighbor
                    degree[v] -= 1
                    # If the neighbor's degree becomes 1, it's a new leaf
                    if degree[v] == 1:
                        leaves.append(v)
        
        # The remaining nodes in the queue are the roots of the MHTs
        return list(leaves)
