class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_val = n
        for left in range(n):
            freq = [0] * (max_val + 3)
            distinct = 0
            consecutive = 0
            for right in range(left, n):
                v = nums[right]
                if freq[v] == 0:
                    distinct += 1
                    if freq[v - 1] > 0:
                        consecutive += 1
                    if freq[v + 1] > 0:
                        consecutive += 1
                freq[v] += 1
                imbalance = distinct - 1 - consecutive
                if imbalance > 0:
                    ans += imbalance
        return ans
