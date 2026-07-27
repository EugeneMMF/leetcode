class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        nums=set()
        for a,b,c in permutations(digits,3):
            if a==0 or c%2!=0: continue
            nums.add(100*a+10*b+c)
        return len(nums)
