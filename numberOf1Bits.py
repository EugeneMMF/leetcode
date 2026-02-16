class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    for i in range(32):
      if n | 1<<i == n:
        count += 1
    return count