import unittest
from mergeSortedArray import Solution

class TestMergeSortedArray(unittest.TestCase):
  def test1(self):
    nums1 = [1,2,3,0,0,0]
    Solution().merge(nums1, m = 3, nums2 = [2,5,6], n = 3)
    self.assertListEqual(nums1, [1,2,2,3,5,6])

  def test2(self):
    nums1 = [1]
    Solution().merge(nums1, m = 1, nums2 = [], n = 0)
    self.assertListEqual(nums1, [1])

  def test3(self):
    nums1 = [0]
    Solution().merge(nums1, m = 0, nums2 = [1], n = 1)
    self.assertListEqual(nums1, [1])

if __name__ == "__main__":
  unittest.main()