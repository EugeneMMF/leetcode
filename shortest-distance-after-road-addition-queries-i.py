  
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import heapq
        
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        result = []
        
        def dijkstra():
            min_heap = [(0, 0)]
            distances = {i: float('inf') for i in range(n)}
            distances[0] = 0
            
            while min_heap:
                current_distance, current_node = heapq.heappop(min_heap)
                if current_distance > distances[current_node]:
                    continue
                for neighbor in graph[current_node]:
                    distance = current_distance + 1
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))
            return distances[n - 1]
        
        for u, v in queries:
            graph[u].append(v)
            shortest_path_length = dijkstra()
            result.append(shortest_path_length)
        
        return result

    
