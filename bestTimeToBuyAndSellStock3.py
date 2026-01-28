from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    forwardProfits = []
    profit = h = 0
    l = prices[0]
    for i in prices:
      if i < l:
        h = l = i
      elif i > h:
        h = i
        profit = max(profit, h-l)
      forwardProfits.append(profit)
    l = h = prices[-1]
    maxP = profit = 0
    for i,p in reversed(list(enumerate(prices))):
      if p > h:
        h = l = p
      elif p < l:
        l = p
        profit = max(profit, h-l)
      maxP = max(maxP, profit + forwardProfits[i])
    return maxP

Solution().maxProfit([1,2,4,2,5,7,2,4,9,0])