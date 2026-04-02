import collections
import heapq

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        adj = collections.defaultdict(list)
        edge_details = {} 

        for u, v, cnti in edges:
            adj[u].append((v, cnti + 1))
            adj[v].append((u, cnti + 1))
            # Store cnti associated with the edge for later calculation of subdivided nodes.
            # Using a sorted tuple (min(u, v), max(u, v)) ensures unique key for an undirected edge.
            edge_details[(min(u, v), max(u, v))] = cnti

        # Dijkstra's algorithm to find the shortest path from node 0 to all original nodes
        dist = {i: float('inf') for i in range(n)}
        dist[0] = 0
        
        # Priority queue stores tuples of (current_distance, node_id)
        pq = [(0, 0)] 

        while pq:
            d, u = heapq.heappop(pq)

            # If we've already found a shorter path to u, skip this one
            if d > dist[u]:
                continue

            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Calculate the total number of reachable nodes
        reachable_count = 0

        # 1. Count original nodes reachable within maxMoves
        for i in range(n):
            if dist[i] <= maxMoves:
                reachable_count += 1

        # 2. Count subdivided nodes reachable within maxMoves
        # Iterate through the original edges to account for the new nodes
        for u, v, cnti in edges:
            # Calculate how many steps can be taken from node u into the subdivision
            # towards v, without exceeding maxMoves or the edge's subdivision length.
            # If u is unreachable (dist[u] is inf), maxMoves - inf is -inf, max(0, -inf) is 0.
            reach_from_u = max(0, maxMoves - dist.get(u, float('inf')))
            
            # Similarly, calculate steps from node v into the subdivision towards u.
            reach_from_v = max(0, maxMoves - dist.get(v, float('inf')))

            # The total number of unique subdivided nodes reachable on this edge
            # is limited by the total number of subdivisions (cnti) and the sum
            # of steps possible from both ends.
            reachable_count += min(cnti, reach_from_u + reach_from_v)
            
        return reachable_count

