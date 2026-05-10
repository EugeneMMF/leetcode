import typing

class Solution:
    def getXORSum(self, arr1: typing.List[int], arr2: typing.List[int]) -> int:
        xor1 = 0
        for num in arr1:
            xor1 ^= num
        xor2 = 0
        for num in arr2:
            xor2 ^= num
        return xor1 & xor2
