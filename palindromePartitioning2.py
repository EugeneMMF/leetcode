class Solution:
  def minCut(self, s: str) -> int:
    def isPalindrome(string):
      return string == string[::-1]

    minCuts: dict[int,int] = {-1: -1, 0: 0} # stores the min cut values for the string up to the index as the key
    cuts = len(s) - 1 # initial minimum cuts if there are no palindromes in s
    backTracker = 0
    isBacking = False
    for i in range(1, len(s)):
      minCuts[i] = minCuts[i-1]
      while backTracker >= 0:
        if minCuts[backTracker-1] < minCuts[i]:
          if isPalindrome(s[backTracker:i+1]):
            minCuts[i] = minCuts[backTracker-1]
        backTracker -= 1
      minCuts[i] += 1
      backTracker = i
    return minCuts[len(s)-1]

print(Solution().minCut("abcccb"))