class Solution:
  def convert_to_integer(self, num: str) -> int:
    result = 0
    for ind,digit in enumerate(reversed(num)):
      digit = ord(digit) - ord("0")
      result += digit * (10**ind)
    return result

  def multiply(self, num1: str, num2: str) -> str:
    num1 = self.convert_to_integer(num1)
    num2 = self.convert_to_integer(num2)
    return str(num1 * num2)