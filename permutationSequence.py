class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s = ""
    digits = list(range(1, n+1))
    tk = k
    for i in reversed(list(range(n))):
      t = factorials[i]
      ind = int((tk-1) / t)
      s += str(digits[ind])
      digits.remove(digits[ind])
      tk -= ind * t
    return s

print(Solution().getPermutation(3,3))