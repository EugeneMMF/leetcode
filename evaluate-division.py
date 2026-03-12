from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            numerator, denominator = equations[i][0], equations[i][1]
            value = values[i]
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value

        results = []

        def dfs(start_node, target_node, current_product, visited):
            if start_node == target_node:
                return current_product

            visited.add(start_node)

            for neighbor, weight in graph[start_node].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target_node, current_product * weight, visited)
                    if res != -1.0:
                        return res
            
            return -1.0

        for query_numerator, query_denominator in queries:
            if query_numerator not in graph or query_denominator not in graph:
                results.append(-1.0)
            elif query_numerator == query_denominator:
                results.append(1.0)
            else:
                visited = set()
                result = dfs(query_numerator, query_denominator, 1.0, visited)
                results.append(result)
        
        return results
