class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, target in enumerate(edges):
            scores[target] += i
        max_score = max(scores)
        for i, s in enumerate(scores):
            if s == max_score:
                return i