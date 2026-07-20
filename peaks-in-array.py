class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        bit = [0] * (n + 1)

        def add(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & -i

        def prefix(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def range_sum(l, r):
            return prefix(r) - prefix(l - 1)

        isPeak = [0] * n
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                isPeak[i] = 1
                add(i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                if r - l + 1 < 3:
                    ans.append(0)
                else:
                    ans.append(range_sum(l + 1, r - 1))
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                for i in (idx - 1, idx, idx + 1):
                    if 1 <= i <= n - 2:
                        new = 1 if nums[i] > nums[i - 1] and nums[i] > nums[i + 1] else 0
                        if new != isPeak[i]:
                            add(i, new - isPeak[i])
                            isPeak[i] = new
        return ans
