class Solution:
    def assignElements(self, groups, elements):
        max_val = max(groups) if groups else 0
        ans = [-1] * (max_val + 1)
        min_idx = {}
        for i, v in enumerate(elements):
            if v not in min_idx or i < min_idx[v]:
                min_idx[v] = i
        pairs = sorted((idx, v) for v, idx in min_idx.items())
        for idx, v in pairs:
            step = v
            for m in range(step, max_val + 1, step):
                if ans[m] == -1:
                    ans[m] = idx
        return [ans[g] for g in groups]