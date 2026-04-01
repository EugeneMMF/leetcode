from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        
        visited = set()
        q = deque()
        
        visited.add(0)
        q.append(0)
        
        while q:
            current_room = q.popleft()
            
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        
        return len(visited) == n
