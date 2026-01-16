import re

class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    pattern = r"?".join(word2) + r"?"
    print(pattern)
    return re.findall(pattern, word1)

print(Solution().minDistance("horse", "ros"))