class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        ans = [0] * len(queries)
        max_beauty = 0
        i = 0
        n = len(items)
        for idx, q in sorted_queries:
            while i < n and items[i][0] <= q:
                if items[i][1] > max_beauty:
                    max_beauty = items[i][1]
                i += 1
            ans[idx] = max_beauty
        return ans