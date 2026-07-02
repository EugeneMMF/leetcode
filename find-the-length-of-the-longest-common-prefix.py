class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref1 = [set() for _ in range(10)]
        pref2 = [set() for _ in range(10)]
        for n in arr1:
            s = str(n)
            for i in range(1, len(s) + 1):
                pref1[i].add(s[:i])
        for n in arr2:
            s = str(n)
            for i in range(1, len(s) + 1):
                pref2[i].add(s[:i])
        for l in range(9, 0, -1):
            if pref1[l] & pref2[l]:
                return l
        return 0