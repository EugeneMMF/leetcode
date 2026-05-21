class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        unique_nums = sorted(set(nums))
        total = 0
        prev = 0
        for num in unique_nums:
            if num > prev + 1:
                gap = num - prev - 1
                take = min(k, gap)
                first = prev + 1
                last = first + take - 1
                total += (first + last) * take // 2
                k -= take
                if k == 0:
                    return total
            prev = num
        if k > 0:
            first = prev + 1
            last = first + k - 1
            total += (first + last) * k // 2
        return total
