class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n
        cur = node1
        step = 0
        while cur != -1 and dist1[cur] == -1:
            dist1[cur] = step
            step += 1
            cur = edges[cur]
        cur = node2
        step = 0
        while cur != -1 and dist2[cur] == -1:
            dist2[cur] = step
            step += 1
            cur = edges[cur]
        best = -1
        bestDist = float('inf')
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                d = max(dist1[i], dist2[i])
                if d < bestDist or (d == bestDist and i < best):
                    bestDist = d
                    best = i
        return best