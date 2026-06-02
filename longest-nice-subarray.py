class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bitcount = [0] * 32
        mask = 0
        left = 0
        best = 0
        for right, val in enumerate(nums):
            while mask & val:
                leftval = nums[left]
                tmp = leftval
                while tmp:
                    lowbit = tmp & -tmp
                    pos = lowbit.bit_length() - 1
                    bitcount[pos] -= 1
                    if bitcount[pos] == 0:
                        mask &= ~(1 << pos)
                    tmp ^= lowbit
                left += 1
            tmp = val
            while tmp:
                lowbit = tmp & -tmp
                pos = lowbit.bit_length() - 1
                bitcount[pos] += 1
                mask |= 1 << pos
                tmp ^= lowbit
            best = max(best, right - left + 1)
        return best
