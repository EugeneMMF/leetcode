class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            s = str(n)
            m = max(s)
            total += int(m * len(s))
        return total
