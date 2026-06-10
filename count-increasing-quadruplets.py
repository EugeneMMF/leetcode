class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        total = 0
        for k in range(2, n - 1):
            pref_counts = [0] * k
            count_less = 0
            for j in range(k):
                pref_counts[j] = count_less
                if nums[j] < nums[k]:
                    count_less += 1
            arr = []
            for j in range(k):
                if nums[j] > nums[k]:
                    arr.append((nums[j], pref_counts[j]))
            arr.sort(key=lambda x: x[0])
            vals = [x[0] for x in arr]
            prefix = [0]
            for _, c in arr:
                prefix.append(prefix[-1] + c)
            for l in range(k + 1, n):
                idx = __import__('bisect').bisect_left(vals, nums[l])
                total += prefix[idx]
        return total