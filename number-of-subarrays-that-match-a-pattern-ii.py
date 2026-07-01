class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        if m == 0 or n <= m:
            return 0
        rel = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                rel[i] = 1
            elif nums[i + 1] == nums[i]:
                rel[i] = 0
            else:
                rel[i] = -1
        # KMP prefix function for pattern
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
        # KMP search over rel
        count = 0
        j = 0
        for i in range(len(rel)):
            while j > 0 and rel[i] != pattern[j]:
                j = pi[j - 1]
            if rel[i] == pattern[j]:
                j += 1
            if j == m:
                count += 1
                j = pi[j - 1]
        return count
