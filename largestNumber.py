from typing import List

class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    def compare(a,b):
      if a+b > b+a: return True
      return False

    def mergeSort(values, fn):
      l = len(values)
      h = l // 2
      if l > 1:
        res = []
        left = mergeSort(values[:h], fn)
        right = mergeSort(values[h:], fn)
        l,ll = 0,len(left)
        r,lr = 0,len(right)
        while l<ll and r<lr:
          if fn(left[l], right[r]):
            res.append(left[l])
            l+=1
          else:
            res.append(right[r])
            r+=1
        while l<ll:
          res.append(left[l])
          l+=1
        while r<lr:
          res.append(right[r])
          r+=1
        return res
      else:
        return values

    nums = [str(num) for num in nums]
    nums = mergeSort(nums, compare)
    if nums[0][0] == '0': return "0"
    return ''.join(nums)