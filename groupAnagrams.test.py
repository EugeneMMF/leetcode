import unittest
from groupAnagrams import Solution

class TestGroupAnagrams(unittest.TestCase):
  def test1(self):
    self.assertListEqual(
      Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]),
      [["bat"],["nat","tan"],["ate","eat","tea"]]
    )

  def test2(self):
    self.assertListEqual(
      Solution().groupAnagrams([""]),
      [[""]]
    )

  def test3(self):
    self.assertListEqual(
      Solution().groupAnagrams(["a"]),
      [["a"]]
    )

if "__main__" == __name__:
  unittest.main()