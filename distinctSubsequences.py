class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    arr = [[-1]*len(t) for _ in range(len(s))]
    s = list(s)
    t = list(t)

    def helper(i, j):
      if j < 0: return 1
      if i < 0: return 0
      if arr[i][j] != -1: return arr[i][j]
      if s[i] == t[j]:
        arr[i][j] = helper(i-1, j-1) + helper(i-1, j)
        return arr[i][j]
      arr[i][j] = helper(i-1, j)
      return arr[i][j]

    print("  " + "  ".join(t))
    helper(len(s)-1, len(t)-1)
    for j,row in enumerate(arr):
      print(s[j] + " " + "  ".join(str(i) for i in row))

print(Solution().numDistinct("rabbbit", "rabbit"))