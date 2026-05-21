class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 1
        while size < n:
            size <<= 1
        pref = [0] * (2 * size)
        suff = [0] * (2 * size)
        mx = [0] * (2 * size)
        cl = [''] * (2 * size)
        cr = [''] * (2 * size)
        seg_size = [0] * (2 * size)
        for i in range(n):
            pref[size + i] = 1
            suff[size + i] = 1
            mx[size + i] = 1
            cl[size + i] = s[i]
            cr[size + i] = s[i]
            seg_size[size + i] = 1
        for i in range(size - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            seg_size[i] = seg_size[left] + seg_size[right]
            cl[i] = cl[left]
            cr[i] = cr[right]
            pref[i] = pref[left]
            if pref[left] == seg_size[left] and cl[left] == cl[right]:
                pref[i] = seg_size[left] + pref[right]
            suff[i] = suff[right]
            if suff[right] == seg_size[right] and cr[left] == cr[right]:
                suff[i] = seg_size[right] + suff[left]
            cross = 0
            if cr[left] == cl[right]:
                cross = suff[left] + pref[right]
            mx[i] = max(mx[left], mx[right], cross)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            pos = size + idx
            pref[pos] = 1
            suff[pos] = 1
            mx[pos] = 1
            cl[pos] = ch
            cr[pos] = ch
            while pos > 1:
                pos >>= 1
                left = 2 * pos
                right = 2 * pos + 1
                seg_size[pos] = seg_size[left] + seg_size[right]
                cl[pos] = cl[left]
                cr[pos] = cr[right]
                pref[pos] = pref[left]
                if pref[left] == seg_size[left] and cl[left] == cl[right]:
                    pref[pos] = seg_size[left] + pref[right]
                suff[pos] = suff[right]
                if suff[right] == seg_size[right] and cr[left] == cr[right]:
                    suff[pos] = seg_size[right] + suff[left]
                cross = 0
                if cr[left] == cl[right]:
                    cross = suff[left] + pref[right]
                mx[pos] = max(mx[left], mx[right], cross)
            res.append(mx[1])
        return res
