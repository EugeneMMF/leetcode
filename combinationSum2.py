from typing import List

class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    memo = {}
    candidates_count = {}
    for candidate in candidates:
      candidates_count[candidate] = candidates_count.get(candidate, 0) + 1

    def solve(target) -> set[list[int]]:
      if memo.get(target): return memo[target]
      result = []
      for i in candidates:
        remainder = target
        if i > remainder:
          break
        remainder -= i
        if remainder == 0:
          if [i] not in result:
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

    results = list(solve(target)[0])
    final = []
    for result in results:
      count = {}
      for item in result:
        count[item] = count.get(item, 0) + 1
      fine = True
      for item in count.keys():
        if count[item] > candidates_count[item]:
          fine = False
          break
      if fine:
        final.append(result)
    return final