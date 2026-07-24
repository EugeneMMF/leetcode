class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)
        lazy = [0] * (2 * size)

        for i in range(n):
            seg[size + i] = nums[i]
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        if seg[1] <= 0:
            return 0

        def push(idx):
            if lazy[idx]:
                val = lazy[idx]
                seg[2 * idx] += val
                seg[2 * idx + 1] += val
                lazy[2 * idx] += val
                lazy[2 * idx + 1] += val
                lazy[idx] = 0

        def range_add(l, r, val, idx, left, right):
            if l > right or r < left:
                return
            if l <= left and right <= r:
                seg[idx] += val
                lazy[idx] += val
                return
            push(idx)
            mid = (left + right) // 2
            range_add(l, r, val, 2 * idx, left, mid)
            range_add(l, r, val, 2 * idx + 1, mid + 1, right)
            seg[idx] = max(seg[2 * idx], seg[2 * idx + 1])

        for i, (l, r, val) in enumerate(queries, 1):
            range_add(l, r, -val, 1, 0, size - 1)
            if seg[1] <= 0:
                return i
        return -1
