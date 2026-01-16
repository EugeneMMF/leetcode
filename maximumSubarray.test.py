import unittest
from maximumSubarray import Solution

class TestMaximumSubarray(unittest.TestCase):
  solver = Solution()
  def test1(self):
    self.assertEqual(self.solver.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

  def test2(self):
    self.assertEqual(self.solver.maxSubArray([1]), 1)

  def test3(self):
    self.assertEqual(self.solver.maxSubArray([5,4,-1,7,8]), 23)

  def test4(self):
    self.assertEqual(self.solver.maxSubArray([-5,-4,1,-7,-8]), 1)

  def test5(self):
    self.assertEqual(self.solver.maxSubArray([-2,1,0]), 1)

  def test6(self):
    self.assertEqual(self.solver.maxSubArray([-1,3,-1]), 3)

  def test7(self):
    self.assertEqual(self.solver.maxSubArray([-1,3,1]), 4)

  def test8(self):
    self.assertEqual(self.solver.maxSubArray([1,2,-1]), 3)

if __name__ == "__main__":
  unittest.main()