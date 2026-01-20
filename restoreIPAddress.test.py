import unittest
from restoreIPAddress import Solution

class TestRestoreIPAddresses(unittest.TestCase):
  def test1(self):
    res = Solution().restoreIpAddresses("25525511135")
    sol = ["255.255.11.135","255.255.111.35"]
    self.assertEqual(len(res), len(sol), "The output and expected solution should have the same length.")
    for ip in sol:
      self.assertIn(ip, res)

  def test2(self):
    res = Solution().restoreIpAddresses("0000")
    sol = ["0.0.0.0"]
    self.assertEqual(len(res), len(sol), "The output and expected solution should have the same length.")
    for ip in sol:
      self.assertIn(ip, res)

  def test3(self):
    res = Solution().restoreIpAddresses("101023")
    sol = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    self.assertEqual(len(res), len(sol), "The output and expected solution should have the same length.")
    for ip in sol:
      self.assertIn(ip, res)

if __name__ == "__main__":
  unittest.main()