import unittest
from grayCode import Solution

class TestMergeSortedArray(unittest.TestCase):
  def test1(self):
    self.assertListEqual(Solution().grayCode(2), [0,1,3,2])

  def test2(self):
    self.assertListEqual(Solution().grayCode(1), [0,1])

if __name__ == "__main__":
  unittest.main()