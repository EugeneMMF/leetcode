import unittest
from rotateImage import Solution

class TestRotateImage(unittest.TestCase):
  def test1(self):
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    self.assertListEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])

  def test2(self):
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(matrix)
    self.assertListEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if "__main__" == __name__:
  unittest.main()