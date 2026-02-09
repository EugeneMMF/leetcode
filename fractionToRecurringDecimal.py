class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0 or denominator == 0: return "0"
    result = "-" if (numerator < 0) ^ (denominator < 0) else ""
    numerator, denominator = abs(numerator), abs(denominator)
    result += str(numerator//denominator)
    if numerator % denominator == 0: return result
    result += "."
    remainders = {}
    rem = numerator % denominator
    while rem and rem not in remainders:
      remainders[rem] = len(result)
      rem *= 10
      result += str(rem//denominator)
      rem %= denominator
    if rem in remainders:
      result = result[:remainders[rem]] + "(" + result[remainders[rem]:] + ")"
    return result

print(Solution().fractionToDecimal(7,-12))