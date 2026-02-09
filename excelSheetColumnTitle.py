class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    mapping = {i: chr(ord("A") + i) for i in range(26)}
    results = []
    while columnNumber:
      columnNumber -= 1
      results.append(mapping[columnNumber%26])
      columnNumber = columnNumber//26
    return "".join(reversed(results))