import typing
class Solution:
    def countMatchingSubarrays(self, nums: typing.List[int], pattern: typing.List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0
        for i in range(n - m):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                if pattern[k] == 1:
                    if b <= a:
                        ok = False
                        break
                elif pattern[k] == 0:
                    if b != a:
                        ok = False
                        break
                else:
                    if b >= a:
                        ok = False
                        break
            if ok:
                count += 1
        return count
