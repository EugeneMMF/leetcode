import unittest
from combinationSum import Solution

class TestCombinationSum(unittest.TestCase):
  def test_1(self):
    solver = Solution()
    inp = [2,3,6,7]
    target = 7
    out = [[2,2,3],[7]]
    res = solver.combinationSum(inp, target)
    self.assertEqual(len(out), len(res))
    for l in out:
      self.assertTrue(l in res)

  def test_2(self):
    solver = Solution()
    inp = [2,3,5]
    target = 8
    out = [[2,2,2,2],[2,3,3],[3,5]]
    res = solver.combinationSum(inp, target)
    self.assertEqual(len(out), len(res))
    for l in out:
      self.assertTrue(l in res)

  def test_3(self):
    solver = Solution()
    inp = [2]
    target = 1
    out = []
    res = solver.combinationSum(inp, target)
    self.assertEqual(len(out), len(res))
    for l in out:
      self.assertTrue(l in res)

if __name__ == "__main__":
  unittest.main()