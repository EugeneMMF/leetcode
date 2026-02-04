from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    numbers = []
    for token in tokens:
      if token  == "*":
        n2,n1 = numbers.pop(), numbers.pop()
        numbers.append(n1*n2)
      elif token  == "+":
        n2,n1 = numbers.pop(), numbers.pop()
        numbers.append(n1+n2)
      elif token  == "-":
        n2,n1 = numbers.pop(), numbers.pop()
        numbers.append(n1-n2)
      elif token  == "/":
        n2,n1 = numbers.pop(), numbers.pop()
        numbers.append(int(n1/n2))
      else:
        numbers.append(int(token))
    return numbers[0]