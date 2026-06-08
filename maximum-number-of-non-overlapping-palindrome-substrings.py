class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        for center in range(n):
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                l -= 1
                r += 1
            l = center
            r = center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                l -= 1
                r += 1
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r
        return count
