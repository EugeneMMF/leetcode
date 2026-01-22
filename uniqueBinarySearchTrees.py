class Solution:
  def numTrees(self, n: int) -> int:
    def factorial(n):
      ans = 1
      for i in range(2,n+1):
        ans *= i
      return ans
    return factorial(2*n)//(factorial(n+1)*factorial(n))

if __name__ == "__main__":
  print(Solution().numTrees(5))