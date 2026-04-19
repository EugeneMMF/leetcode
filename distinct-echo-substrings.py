class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        base1, mod1 = 91138233, 1000000007
        base2, mod2 = 97266353, 1000000009
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base1) % mod1
            pow2[i] = (pow2[i - 1] * base2) % mod2
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        for i, ch in enumerate(text):
            o = ord(ch)
            pref1[i + 1] = (pref1[i] * base1 + o) % mod1
            pref2[i + 1] = (pref2[i] * base2 + o) % mod2
        def get_hash(l, r):
            h1 = (pref1[r] - pref1[l] * pow1[r - l]) % mod1
            h2 = (pref2[r] - pref2[l] * pow2[r - l]) % mod2
            return h1, h2
        seen = set()
        for i in range(n):
            max_h = (n - i) // 2
            for h in range(1, max_h + 1):
                if get_hash(i, i + h) == get_hash(i + h, i + 2 * h):
                    seen.add((get_hash(i, i + 2 * h), 2 * h))
        return len(seen)
