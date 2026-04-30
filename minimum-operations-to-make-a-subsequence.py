class Solution:
    def minOperations(self, target, arr):
        pos = {v:i for i,v in enumerate(target)}
        seq = [pos[x] for x in arr if x in pos]
        import bisect
        lis = []
        for v in seq:
            i = bisect.bisect_left(lis, v)
            if i == len(lis):
                lis.append(v)
            else:
                lis[i] = v
        return len(target) - len(lis)
