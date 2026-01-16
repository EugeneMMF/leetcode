import re

class Solution:
  def isNumber(self, s: str) -> bool:
    def checkNumber(s: str) -> bool:
      regexes = [
        r"[+-]?\.[0-9]+",
        r"[+-]?[0-9]+\.?[0-9]*",
      ]
      return any(re.fullmatch(pattern, s) for pattern in regexes)
    def checkPower(s: str) -> bool:
      return re.fullmatch(r"[+-]?[0-9]+", s) is not None
    s = s.replace("E", "e")
    if "e" in s:
      parts = s.split("e")
      if len(parts) != 2:
        return False
      return checkNumber(parts[0]) and checkPower(parts[1])
    else:
      return checkNumber(s)

for val in ["0", "e", ".", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
  print(val, Solution().isNumber(val))