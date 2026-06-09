class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0:
            return 0
        total_a = total_b = total_c = 0
        for ch in s:
            if ch == 'a':
                total_a += 1
            elif ch == 'b':
                total_b += 1
            else:
                total_c += 1
        if total_a < k or total_b < k or total_c < k:
            return -1
        limit_a = total_a - k
        limit_b = total_b - k
        limit_c = total_c - k
        l = 0
        cnt_a = cnt_b = cnt_c = 0
        max_len = 0
        for r, ch in enumerate(s):
            if ch == 'a':
                cnt_a += 1
            elif ch == 'b':
                cnt_b += 1
            else:
                cnt_c += 1
            while cnt_a > limit_a or cnt_b > limit_b or cnt_c > limit_c:
                ch_l = s[l]
                if ch_l == 'a':
                    cnt_a -= 1
                elif ch_l == 'b':
                    cnt_b -= 1
                else:
                    cnt_c -= 1
                l += 1
            cur_len = r - l + 1
            if cur_len > max_len:
                max_len = cur_len
        return n - max_len
