from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = h = 0
    l = prices[0]
    for i in prices:
      if i < l:
        h = l = i
      elif i > h:
        h = i
        profit = max(profit, h-l)
    return profit