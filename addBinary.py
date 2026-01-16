class Solution:
  def addBinary(self, a: str, b: str):
    count = max(len(a), len(b)) + 1
    a = [*[0]*(count-len(a)), *[int(i) for i in a]]
    b = [*[0]*(count-len(b)), *[int(i) for i in b]]
    res = [0] * count
    carrier = 0
    for i in reversed(list(range(count))):
      val = carrier + a[i] + b[i]
      res[i] = val%2
      carrier = int(val/2)
    if res[0]:
      return "".join(str(i) for i in res)
    return "".join(str(i) for i in res[1:])
    
print(Solution().addBinary("11", "1"))