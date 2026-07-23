
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            child_sizes = []
            count = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    size = dfs(neighbor, node)
                    child_sizes.append(size)
                    count += size
            
            if len(set(child_sizes)) <= 1:
                nonlocal good_node_count
                good_node_count += 1
            
            return count
        
        good_node_count = 0
        dfs(0, -1)
        
        return good_node_count

