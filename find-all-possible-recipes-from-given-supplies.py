class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        indeg = {}
        for r, ing in zip(recipes, ingredients):
            indeg[r] = len(ing)
            for item in ing:
                graph[item].append(r)
        q = deque(supplies)
        res = []
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
                    res.append(nxt)
        return res