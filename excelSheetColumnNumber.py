class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    mapping = {chr(ord("A") + i): i+1 for i in range(26)}
    result = 0
    for c in columnTitle:
      result *= 26
      result += mapping[c]
    return result