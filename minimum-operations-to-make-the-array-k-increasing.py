class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        from bisect import bisect_right
        n = len(arr)
        total_lnds = 0
        for start in range(k):
            tails = []
            i = start
            while i < n:
                x = arr[i]
                idx = bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
                i += k
            total_lnds += len(tails)
        return n - total_lnds
