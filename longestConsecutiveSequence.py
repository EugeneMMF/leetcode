class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    nums = set(nums)
    longest = 0
    for num in nums:
      if num - 1 not in nums:
        count = 1
        while num + 1 in nums:
          count += 1
          num += 1
        longest = max(longest, count)
    return longest