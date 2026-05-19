class Solution:
    def recoverArray(self, nums):
        from collections import Counter
        sorted_nums = sorted(nums)
        n = len(nums) // 2
        min_val = sorted_nums[0]
        candidates = set()
        for v in sorted_nums[1:]:
            diff = v - min_val
            if diff > 0 and diff % 2 == 0:
                candidates.add(diff // 2)
        for k in candidates:
            counter = Counter(sorted_nums)
            arr = []
            for x in sorted_nums:
                if counter[x] == 0:
                    continue
                counter[x] -= 1
                y = x + 2 * k
                if counter[y] == 0:
                    break
                counter[y] -= 1
                arr.append(x + k)
            else:
                return arr
        return []