import unittest
from decodeWays import Solution

class TestDecodeWays(unittest.TestCase):
  def __init__(self, methodName = "runTest"):
    super().__init__(methodName)
    self.solver = Solution()

  def test1(self):
    self.assertEqual(self.solver.numDecodings("12"), 2)

  def test2(self):
    self.assertEqual(self.solver.numDecodings("226"), 3)

  def test3(self):
    self.assertEqual(self.solver.numDecodings("06"), 0)

  def test4(self):
    self.assertEqual(self.solver.numDecodings("2611055971756562"), 4)

if __name__ == "__main__":
  unittest.main()