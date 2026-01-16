from typing import List

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    memo = {}

    def solve(target) -> set[list[int]]:
      if memo.get(target): return memo[target]
      result = []
      for i in candidates:
        remainder = target
        if i > remainder:
          break
        remainder -= i
        if remainder == 0:
          result.append([i])
          continue
        temp = solve(remainder)
        if temp[1]:
          for res in temp[0]:
            new_res = [i, *res]
            new_res.sort()
            if new_res not in result:
              result.append(new_res)
      if len(result) == 0:
        memo[target] = result, False
        return result, False
      else:
        memo[target] = result, True
        return result, True

    return list(solve(target)[0])