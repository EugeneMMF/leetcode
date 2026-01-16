import unittest
from firstMissingPositive import Solution

class TestFirstMissingPositive(unittest.TestCase):
  def test1(self):
    solver = Solution()
    nums = [1,2,0]
    output = solver.firstMissingPositive(nums)
    self.assertEqual(output, 3)

  def test2(self):
    solver = Solution()
    nums = [3,4,-1,1]
    output = solver.firstMissingPositive(nums)
    self.assertEqual(output, 2)

  def test3(self):
    solver = Solution()
    nums = [7,8,9,11,12]
    output = solver.firstMissingPositive(nums)
    self.assertEqual(output, 1)

if __name__ == "__main__":
  unittest.main()