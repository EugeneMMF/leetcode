class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n2 = len(nums)
        n = n2 // 2
        total = sum(nums)
        left = nums[:n]
        right = nums[n:]
        def gen(arr):
            sums = [[] for _ in range(len(arr)+1)]
            sums[0] = [0]
            for v in arr:
                for k in range(len(arr), 0, -1):
                    for s in sums[k-1]:
                        sums[k].append(s+v)
            return sums
        sums_left = gen(left)
        sums_right = gen(right)
        best = float('inf')
        target = total / 2
        import bisect
        for k in range(n+1):
            list1 = sums_left[k]
            list2 = sums_right[n-k]
            list2.sort()
            for s1 in list1:
                need = target - s1
                idx = bisect.bisect_left(list2, need)
                if idx < len(list2):
                    s = s1 + list2[idx]
                    diff = abs(2*s - total)
                    if diff < best:
                        best = diff
                if idx > 0:
                    s = s1 + list2[idx-1]
                    diff = abs(2*s - total)
                    if diff < best:
                        best = diff
        return best