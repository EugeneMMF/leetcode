class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from collections import Counter
        cnt = Counter(nums)
        ans = 0
        for s in nums:
            if target.startswith(s):
                suffix = target[len(s):]
                if suffix in cnt:
                    ans += cnt[suffix]
                    if suffix == s:
                        ans -= 1
        return ans
