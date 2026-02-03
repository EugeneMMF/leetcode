from typing import List

class Solution:
  def candy(self, ratings: List[int]) -> int:
    l = len(ratings)
    candies = [1]*l
    for i in range(1,l):
      if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1
    for i in range(l-2, -1, -1):
      if ratings[i] > ratings[i+1]:
        candies[i] = max(candies[i], candies[i+1]+1)
    return sum(candies)

print(Solution().candy([0,1,2,3,2,1]))