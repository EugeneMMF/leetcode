class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        import sys
        sys.setrecursionlimit(200000)
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        ans = [0] * n
        def dfs(u):
            big_set = {nums[u]}
            min_missing = 1
            if nums[u] == 1:
                while min_missing in big_set:
                    min_missing += 1
            for v in children[u]:
                child_set, child_missing = dfs(v)
                if len(child_set) > len(big_set):
                    big_set, child_set = child_set, big_set
                    min_missing, child_missing = child_missing, min_missing
                for val in child_set:
                    if val not in big_set:
                        big_set.add(val)
                        if val == min_missing:
                            while min_missing in big_set:
                                min_missing += 1
            ans[u] = min_missing
            return big_set, min_missing
        dfs(0)
        return ans