from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for fro, to in tickets:
            graph[fro].append(to)

        for fro in graph:
            graph[fro].sort()

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)
                dfs(next_airport)
            
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]
