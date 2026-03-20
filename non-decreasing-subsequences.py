class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        results = set()
        current_subsequence = []

        def backtrack(start_index):
            if len(current_subsequence) >= 2:
                results.add(tuple(current_subsequence))

            used_in_level = set()
            for i in range(start_index, len(nums)):
                num = nums[i]
                if num in used_in_level:
                    continue

                if not current_subsequence or num >= current_subsequence[-1]:
                    current_subsequence.append(num)
                    backtrack(i + 1)
                    current_subsequence.pop()
                    used_in_level.add(num)
        
        backtrack(0)
        return list(map(list, results))
