class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_map = {}
        for num in nums:
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            if s not in digit_map:
                digit_map[s] = (num, None)
            else:
                max1, max2 = digit_map[s]
                if num >= max1:
                    digit_map[s] = (num, max1)
                elif max2 is None or num > max2:
                    digit_map[s] = (max1, num)
        best = -1
        for max1, max2 in digit_map.values():
            if max2 is not None:
                total = max1 + max2
                if total > best:
                    best = total
        return best