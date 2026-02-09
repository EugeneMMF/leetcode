class Solution:
  def trailingZeroes(self, n: int) -> int:
    parts = [5**i for i in range(1,10)]
    return sum(n//part for part in parts)

print(Solution().trailingZeroes(30))