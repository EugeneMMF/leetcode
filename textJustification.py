from typing import List

class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    lens = [len(word) for word in words]
    result = []
    n = len(words)
    i = 0
    line = []
    count = 0
    while i <= n:
      if i < n and lens[i] <= maxWidth - count:
          line.append(words[i])
          count+=lens[i]+1
          i += 1
      else:
        totalSpaces = maxWidth - sum(len(word) for word in line)
        if len(line) == 0: break
        s = line[0]
        if len(line) > 1:
          spaces = totalSpaces//(len(line)-1)
          rem = totalSpaces%(len(line)-1)
          for j in range(1,len(line)):
            ct = spaces + 1 if j <= rem else spaces
            s += " "*ct + line[j]
        else:
          s += " "*totalSpaces
        line = []
        count = 0
        result.append(s)
        if i == n: i+=1
    lastLine = result.pop()
    lastLine = " ".join(filter(lambda x: x != '', lastLine.split(" ")))
    lastLine += " "*(maxWidth - len(lastLine))
    result.append(lastLine)
    return result

print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))