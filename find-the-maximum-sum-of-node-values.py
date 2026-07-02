class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        pos = []
        neg = []
        for v in nums:
            d = (v ^ k) - v
            if d > 0:
                pos.append(d)
            else:
                neg.append(d)
        pos.sort()
        neg.sort(reverse=True)
        if len(pos) % 2 == 0:
            return total + sum(pos)
        if pos:
            option1 = total + sum(pos) - pos[0]
        else:
            option1 = total
        if neg:
            option2 = total + sum(pos) + neg[0]
        else:
            option2 = total
        return max(option1, option2)