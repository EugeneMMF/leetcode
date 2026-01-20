from typing import List

class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    if len(s) > 12 or len(s) < 4: return []
    s = list(s)

    def check(s: list[str], remainingParts: int) -> List[str|None]:
      ls = len(s)
      if ls > remainingParts * 3 or ls < remainingParts: return []
      if s[0] == "0":
        if ls == 1:
          return s
        returned = check(s[1:], remainingParts-1)
        if returned:
          return ["0." + part for part in returned]
        return []
      if remainingParts == 1:
        part = "".join(s)
        if int(part) <= 255:
          return [part]
        return []
      start = ""
      sols = []
      for i in range(min(3, len(s))):
        start += s[i]
        if int(start) <= 255:
          returned = check(s[i+1:], remainingParts-1)
          if returned:
            sols.extend([f"{start}." + part for part in returned])
      return sols

    return check(s, 4)