from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i1 = 0
    i2 = 0
    sortedList = []
    while i1 < m and i2 < n:
      if nums1[i1] < nums2[i2]:
        sortedList.append(nums1[i1])
        i1 += 1
      else:
        sortedList.append(nums2[i2])
        i2 += 1
    while i1 < m:
      sortedList.append(nums1[i1])
      i1 += 1
    while i2 < n:
      sortedList.append(nums2[i2])
      i2 += 1
    nums1[:] = sortedList[:]