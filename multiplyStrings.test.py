import unittest
from multiplyStrings import Solution

class TestMultiplyStrings(unittest.TestCase):
  def test_1(self):
    num1 = "2"
    num2 = "3"
    expected_output = "6"
    output = Solution().multiply(num1, num2)
    self.assertEqual(output, expected_output)

  def test_2(self):
    num1 = "123"
    num2 = "456"
    expected_output = "56088"
    output = Solution().multiply(num1, num2)
    self.assertEqual(output, expected_output)

if __name__ == "__main__":
  unittest.main()