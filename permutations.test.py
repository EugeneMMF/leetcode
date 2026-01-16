import unittest
from permutations import Solution

class TestPermutations(unittest.TestCase):
  def test1(self):
    self.assertListEqual(Solution().permute([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

  def test2(self):
    self.assertListEqual(Solution().permute([0,1]), [[0,1],[1,0]])

  def test3(self):
    self.assertListEqual(Solution().permute([1]), [[1]])

if "__main__" == __name__:
  unittest.main()