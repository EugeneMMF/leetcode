class Solution:
    def flipgame(self, fronts, backs):
        bad = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        candidates = [x for x in fronts + backs if x not in bad]
        return min(candidates) if candidates else 0
