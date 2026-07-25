class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])
        ends = [r for _, r, _, _ in arr]
        from bisect import bisect_left
        dp_sum = [[0] * 5 for _ in range(n)]
        dp_list = [[()] * 5 for _ in range(n)]
        for i, (l, r, w, idx) in enumerate(arr):
            p = bisect_left(ends, l) - 1
            for k in range(5):
                if i > 0:
                    dp_sum[i][k] = dp_sum[i-1][k]
                    dp_list[i][k] = dp_list[i-1][k]
                else:
                    dp_sum[i][k] = 0
                    dp_list[i][k] = ()
            for k in range(1, 5):
                if p >= 0:
                    prev_sum = dp_sum[p][k-1]
                    prev_list = dp_list[p][k-1]
                else:
                    if k-1 == 0:
                        prev_sum = 0
                        prev_list = ()
                    else:
                        continue
                cand_sum = w + prev_sum
                cand_list = tuple(sorted(prev_list + (idx,)))
                cur_sum = dp_sum[i][k]
                cur_list = dp_list[i][k]
                if cand_sum > cur_sum or (cand_sum == cur_sum and cand_list < cur_list):
                    dp_sum[i][k] = cand_sum
                    dp_list[i][k] = cand_list
        best_sum = -1
        best_list = ()
        for k in range(1, 5):
            s = dp_sum[n-1][k]
            l = dp_list[n-1][k]
            if s > best_sum or (s == best_sum and l < best_list):
                best_sum = s
                best_list = l
        return list(best_list)
