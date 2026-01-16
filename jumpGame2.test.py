import unittest
from jumpGame2 import Solution

class TestJumpGame2(unittest.TestCase):
  def test1(self):
    inp = [2,3,1,1,4]
    self.assertEqual(Solution().jump(inp), 2)

  def test2(self):
    inp = [2,3,0,1,4]
    self.assertEqual(Solution().jump(inp), 2)

  def test3(self):
    inp = [3,2,1]
    self.assertEqual(Solution().jump(inp), 1)

  def test4(self):
    inp = [1,2,3]
    self.assertEqual(Solution().jump(inp), 2)

  def test5(self):
    inp = [2,3,1]
    self.assertEqual(Solution().jump(inp), 1)

  def test6(self):
    inp = [10,9,8,7,6,5,4,3,2,1,1,0]
    self.assertEqual(Solution().jump(inp), 2)


if "__main__" == __name__:
  unittest.main()