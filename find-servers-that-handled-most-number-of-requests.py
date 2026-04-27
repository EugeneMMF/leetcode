class Solution:
    def busiestServers(self, k, arrival, load):
        import heapq, bisect
        available = list(range(k))
        cnt = [0] * k
        busy = []
        for i, (t, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                end, s = heapq.heappop(busy)
                idx = bisect.bisect_left(available, s)
                if idx == len(available) or available[idx] != s:
                    available.insert(idx, s)
            if not available:
                continue
            start = i % k
            idx = bisect.bisect_left(available, start)
            if idx == len(available):
                idx = 0
            s = available.pop(idx)
            cnt[s] += 1
            heapq.heappush(busy, (t + l, s))
        mx = max(cnt)
        return [i for i, c in enumerate(cnt) if c == mx]
