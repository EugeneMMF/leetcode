class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        import bisect
        logs.sort(key=lambda e: e[1])
        queries_with_idx = sorted(enumerate(queries), key=lambda e: e[1])
        last_time = [0] * (n + 1)
        times = [0] * n
        for i in range(n):
            times[i] = 0
        times.sort()
        res = [0] * len(queries)
        log_idx = 0
        for qi, q in queries_with_idx:
            while log_idx < len(logs) and logs[log_idx][1] <= q:
                srv, t = logs[log_idx]
                old = last_time[srv]
                pos = bisect.bisect_left(times, old)
                times.pop(pos)
                bisect.insort(times, t)
                last_time[srv] = t
                log_idx += 1
            threshold = q - x
            idx = bisect.bisect_left(times, threshold)
            res[qi] = idx
        return res
