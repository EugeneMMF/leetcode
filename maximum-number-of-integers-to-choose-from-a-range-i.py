class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total = 0
        count = 0
        for i in range(1, n + 1):
            if i in banned_set:
                continue
            if total + i > maxSum:
                break
            total += i
            count += 1
        return count
