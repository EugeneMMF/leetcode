from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    temp = {}
    for str in strs:
      key = "".join(sorted(str))
      temp[key] = temp.get(key, []).append(str)
    return list(temp.values())