from typing import List

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    s = list(s)
    palindromes = {}

    def isPalindrome(string):
      palindromes[string] = p = palindromes.get(string, string == "".join(reversed(string)))
      return p

    def helper(start, end):
      solutions = [s[start:end]]
      for i in range(1, end - start + 1):
        word = "".join(s[start:start+i])
        if isPalindrome(word):
          solutions.extend([[word]+j for j in helper(start+i, end)])
      return solutions

    return list(set(tuple(j) for j in helper(0, len(s))))

print(Solution().partition("aab"))