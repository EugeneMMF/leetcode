import bisect

class MinStack:
  def __init__(self):
    self.stack = []
    self.sortedStack = []

  def push(self, val: int) -> None:
    bisect.insort(self.sortedStack, val)
    self.stack.append(val)

  def pop(self) -> None:
    t = self.stack.pop()
    self.sortedStack.remove(t)
    return t

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.sortedStack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()