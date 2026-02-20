from string import ascii_letters

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    start = 0
    end = 0
    solution = ""
    countT = {}
    countSeen = {}
    total = len(t)
    for c in t:
      countT[c] = countT.get(c, 0) + 1
      countSeen[c] = 0
    for i,c in enumerate(s):
      if c in countT:
        end = i+1
        if countT[c] > countSeen[c]:
          total -= 1
        countSeen[c] += 1
        if total == 0:
          if solution == '':
            solution = s[start:end]
          else:
            solution = s[start:end] if (end - start) < len(solution) else solution
          while total == 0:
            if s[start] in countSeen:
              countSeen[s[start]] -= 1
              if countSeen[s[start]] < countT[s[start]]:
                total += 1
            solution = s[start:end] if (end - start) < len(solution) else solution
            start += 1
    return solution