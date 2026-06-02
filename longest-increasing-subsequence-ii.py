class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_val = 100000
        size = 1
        while size <= max_val:
            size <<= 1
        seg = [0] * (2 * size)
        def update(pos, val):
            idx = pos + size
            if seg[idx] >= val:
                return
            seg[idx] = val
            idx //= 2
            while idx:
                seg[idx] = seg[2 * idx] if seg[2 * idx] >= seg[2 * idx + 1] else seg[2 * idx + 1]
                idx //= 2
        def query(l, r):
            if l > r:
                return 0
            l += size
            r += size
            res = 0
            while l <= r:
                if l & 1:
                    if seg[l] > res:
                        res = seg[l]
                    l += 1
                if not (r & 1):
                    if seg[r] > res:
                        res = seg[r]
                    r -= 1
                l //= 2
                r //= 2
            return res
        best = 0
        for num in nums:
            start = num - k
            if start < 1:
                start = 1
            prev = query(start, num - 1)
            cur = prev + 1
            if cur > best:
                best = cur
            update(num, cur)
        return best