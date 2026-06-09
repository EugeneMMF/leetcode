class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        indices = [i for i, w in enumerate(words) if w == target]
        if not indices:
            return -1
        min_dist = n
        for i in indices:
            diff = abs(i - startIndex)
            dist = min(diff, n - diff)
            if dist < min_dist:
                min_dist = dist
        return min_dist