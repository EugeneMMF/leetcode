from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    totalProfit = 0
    l = h = prices[0]
    for i in prices[1:]:
      if i < h:
        totalProfit += profit
        profit = 0
        l = h = i
      else:
        if i < l:
          l = i
          h = i
        profit = max(profit, i - l)
    return totalProfit + profit