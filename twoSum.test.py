import unittest
from twoSum import Solution

class TestTwoSum(unittest.TestCase):
  def test_1(self):
    solver = Solution()
    nums = [2,7,11,15]
    target = 9
    expected_output = [0,1]
    output = solver.twoSum(nums, target)
    self.assertEqual(output, expected_output, "Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].")

  def test_2(self):
    solver = Solution()
    nums = [3,2,4]
    target = 6
    expected_output = [1,2]
    output = solver.twoSum(nums, target)
    self.assertEqual(output, expected_output, "Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].")

  def test_3(self):
    solver = Solution()
    nums = [3,3]
    target = 6
    expected_output = [0,1]
    output = solver.twoSum(nums, target)
    self.assertEqual(output, expected_output, "Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].")

if __name__ == "__main__":
  unittest.main()