import unittest
from partitionList import Solution, ListNode

def testArray(arr, x):
  if not arr:
    start = None
    current = start
  else:
    start = ListNode(arr[0])
    current = start
    for i in arr[1:]:
      current.next = ListNode(i)
      current = current.next
  sol = Solution().partition(start, x)
  current = sol
  if not current:
    return current
  s = [current.val]
  while current.next:
    current = current.next
    s.append(current.val)
  return s

class TestPartitionList(unittest.TestCase):
  def test1(self):
    self.assertListEqual(testArray([1,4,3,2,5,2], 3), [1,2,2,4,3,5])

  def test2(self):
    self.assertListEqual(testArray([2,1], 2), [1,2])

  def test3(self):
    self.assertEqual(testArray([], 0), None)


if __name__ == "__main__":
  unittest.main()