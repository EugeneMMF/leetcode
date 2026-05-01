class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cnt_a = [0] * 26
        cnt_b = [0] * 26
        for ch in a:
            cnt_a[ord(ch) - 97] += 1
        for ch in b:
            cnt_b[ord(ch) - 97] += 1
        pref_a = [0] * 26
        pref_b = [0] * 26
        pref_a[0] = cnt_a[0]
        pref_b[0] = cnt_b[0]
        for i in range(1, 26):
            pref_a[i] = pref_a[i - 1] + cnt_a[i]
            pref_b[i] = pref_b[i - 1] + cnt_b[i]
        total_a = len(a)
        total_b = len(b)
        best = total_a + total_b
        for t in range(25):
            cost1 = (total_a - pref_a[t]) + pref_b[t]
            cost2 = (total_b - pref_b[t]) + pref_a[t]
            if cost1 < best:
                best = cost1
            if cost2 < best:
                best = cost2
        cost3 = (total_a - max(cnt_a)) + (total_b - max(cnt_b))
        if cost3 < best:
            best = cost3
        return best
