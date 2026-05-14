import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends = [(arr, leave, i) for i, (arr, leave) in enumerate(times)]
        friends.sort(key=lambda x: x[0])
        occupied = []
        free = []
        next_chair = 0
        target_chair = 0
        for arr, leave, idx in friends:
            while occupied and occupied[0][0] <= arr:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free, chair)
            if free:
                chair = heapq.heappop(free)
            else:
                chair = next_chair
                next_chair += 1
            heapq.heappush(occupied, (leave, chair))
            if idx == targetFriend:
                target_chair = chair
        return target_chair
