from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}
        for v in nums2:
            self.freq[v] = self.freq.get(v, 0) + 1

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.freq[old] -= 1
        if self.freq[old] == 0:
            del self.freq[old]
        new = old + val
        self.nums2[index] = new
        self.freq[new] = self.freq.get(new, 0) + 1

    def count(self, tot: int) -> int:
        res = 0
        for x in self.nums1:
            res += self.freq.get(tot - x, 0)
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
