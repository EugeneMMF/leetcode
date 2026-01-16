class Solution:
  def countAndSay(self, n: int) -> str:
    if n == 1:
      return "1"
    previous_result = self.countAndSay(n-1)
    result = ""
    count = 0
    prev = previous_result[0]
    for char in previous_result:
      if char == prev:
        count += 1
      else:
        result += f"{count}{prev}"
        count = 1
        prev = char
    result += f"{count}{prev}"
    return result