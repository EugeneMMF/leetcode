class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        s_count = Counter(s)
        t_count = Counter(target)
        min_copies = float('inf')
        for ch, t_need in t_count.items():
            if ch not in s_count:
                return 0
            min_copies = min(min_copies, s_count[ch] // t_need)
        return min_copies if min_copies != float('inf') else 0