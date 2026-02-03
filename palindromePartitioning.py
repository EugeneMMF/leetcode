from typing import List

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    def isPalindrome(string):
      return string == string[::-1]

    def helper(start, end):
      if end - start == 1: return [[s[start:end]]]
      if end - start == 0: return [[]]
      solutions = []
      for i in range(1, end - start + 1):
        word = s[start:start+i]
        if isPalindrome(word):
          solutions.extend([[word]+j for j in helper(start+i, end)])
      return solutions

    return helper(0, len(s))

print(Solution().partition("aab"))