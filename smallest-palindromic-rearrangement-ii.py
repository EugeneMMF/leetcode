class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from math import comb
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        half_counts = {ch: cnt // 2 for ch, cnt in freq.items()}
        n = len(s) // 2
        cap = k + 1
        def count_perms(counts, remaining):
            res = 1
            for v in counts.values():
                if v == 0:
                    continue
                res *= comb(remaining, v)
                if res >= cap:
                    return cap
                remaining -= v
            return res
        total_perm = count_perms(half_counts, n)
        if total_perm < k:
            return ""
        sorted_chars = sorted(half_counts.keys())
        half = []
        for _ in range(n):
            for ch in sorted_chars:
                if half_counts[ch] == 0:
                    continue
                half_counts[ch] -= 1
                cnt = count_perms(half_counts, n - len(half) - 1)
                if cnt < k:
                    k -= cnt
                    half_counts[ch] += 1
                else:
                    half.append(ch)
                    break
        mid = ""
        for ch, cnt in freq.items():
            if cnt % 2 == 1:
                mid = ch
                break
        return "".join(half) + mid + "".join(reversed(half))
