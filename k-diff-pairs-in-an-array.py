class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if k == 0:
            from collections import Counter
            counts = Counter(nums)
            result = 0
            for num, freq in counts.items():
                if freq >= 2:
                    result += 1
            return result
        else:
            unique_nums = set(nums)
            result = 0
            for num in unique_nums:
                if (num + k) in unique_nums:
                    result += 1
            return result
