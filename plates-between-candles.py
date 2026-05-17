class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        from bisect import bisect_left, bisect_right
        n = len(s)
        plates_prefix = [0] * n
        for i, ch in enumerate(s):
            plates_prefix[i] = plates_prefix[i-1] + (1 if ch == '*' else 0) if i > 0 else (1 if ch == '*' else 0)
        candles = [i for i, ch in enumerate(s) if ch == '|']
        res = []
        for l, r in queries:
            left_idx = bisect_left(candles, l)
            right_idx = bisect_right(candles, r) - 1
            if left_idx < len(candles) and right_idx >= 0 and left_idx <= right_idx:
                left_candle = candles[left_idx]
                right_candle = candles[right_idx]
                if left_candle < right_candle:
                    plates_between = plates_prefix[right_candle-1] - plates_prefix[left_candle]
                    res.append(plates_between)
                    continue
            res.append(0)
        return res