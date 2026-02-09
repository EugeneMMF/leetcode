class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    version1 = [int(i) for i in version1.split(".")]
    version2 = [int(i) for i in version2.split(".")]
    maxL = max(len(version1), len(version2))
    version1 += [0]*(maxL - len(version1))
    version2 += [0]*(maxL - len(version2))
    for v1,v2 in zip(version1, version2):
      if v1 > v2: return 1
      if v2 > v1: return -1
    return 0