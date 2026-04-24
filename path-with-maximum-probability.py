class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        import heapq
        adj=[[] for _ in range(n)]
        for (a,b),p in zip(edges,succProb):
            adj[a].append((b,p))
            adj[b].append((a,p))
        prob=[0.0]*n
        prob[start_node]=1.0
        heap=[(-1.0,start_node)]
        while heap:
            cur_prob,u=heapq.heappop(heap)
            cur_prob=-cur_prob
            if u==end_node:
                return cur_prob
            if cur_prob<prob[u]:
                continue
            for v,p in adj[u]:
                new_prob=cur_prob*p
                if new_prob>prob[v]:
                    prob[v]=new_prob
                    heapq.heappush(heap,(-new_prob,v))
        return 0.0
