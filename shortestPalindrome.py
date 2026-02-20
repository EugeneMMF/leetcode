class Solution:
  def shortestPalindrome(self, s: str) -> str:
    l = len(s)
    reversedString = s[::-1]
    for i in range(l):
      if s[:l-i] == reversedString[i:]:
        return reversedString[:i] + s
    return ""

print(Solution().shortestPalindrome("abcd"))