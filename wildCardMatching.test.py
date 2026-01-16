import unittest
from wildCardMatching import Solution

class TestWildCardMatching(unittest.TestCase):
  def test_1(self):
    s = "aa"
    p = "a"
    self.assertEqual(Solution().isMatch(s, p), False)

  def test_2(self):
    s = "aa"
    p = "*"
    self.assertEqual(Solution().isMatch(s, p), True)

  def test_3(self):
    s = "cb"
    p = "?a"
    self.assertEqual(Solution().isMatch(s, p), False)

  def test_4(self):
    s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
    p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
    self.assertEqual(Solution().isMatch(s, p), True)

  def test_5(self):
    s = "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
    p = "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"
    self.assertEqual(Solution().isMatch(s, p), False)

if "__main__" == __name__:
  unittest.main()