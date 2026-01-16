from countAndSay import Solution
import unittest

class TestCountAndSay(unittest.TestCase):
  def test_1(self):
    solver = Solution()
    result = solver.countAndSay(1)
    self.assertEqual(result, "1")

  def test_2(self):
    solver = Solution()
    result = solver.countAndSay(2)
    self.assertEqual(result, "11")

  def test_3(self):
    solver = Solution()
    result = solver.countAndSay(3)
    self.assertEqual(result, "21")

  def test_4(self):
    solver = Solution()
    result = solver.countAndSay(4)
    self.assertEqual(result, "1211")

if "__main__" == __name__:
  unittest.main()