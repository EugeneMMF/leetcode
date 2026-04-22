class Solution:
    def kthSmallest(self, mat, k):
        import heapq
        sums = mat[0][:k]
        for row in mat[1:]:
            new = []
            heap = []
            limit = min(len(sums), k)
            for i in range(limit):
                heapq.heappush(heap, (sums[i] + row[0], i, 0))
            while len(new) < k and heap:
                s, i, j = heapq.heappop(heap)
                new.append(s)
                if j + 1 < len(row):
                    heapq.heappush(heap, (sums[i] + row[j + 1], i, j + 1))
            sums = new
        return sums[k - 1] if k <= len(sums) else sums[-1]
