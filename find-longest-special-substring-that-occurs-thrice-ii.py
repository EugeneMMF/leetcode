class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        runs = [[] for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            runs[ord(s[i]) - 97].append(length)
            i = j
        best = 0
        for lst in runs:
            if not lst:
                continue
            max_len = max(lst)
            lo, hi = 1, max_len
            ans = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                total = 0
                for l in lst:
                    if l >= mid:
                        total += l - mid + 1
                if total >= 3:
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if ans > best:
                best = ans
        return best if best > 0 else -1