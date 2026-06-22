class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = [0] * 50
        neg_count = 0
        for i in range(k):
            v = nums[i]
            if v < 0:
                freq[-v - 1] += 1
                neg_count += 1
        def get_beauty():
            if neg_count < x:
                return 0
            cnt = 0
            for idx in range(49, -1, -1):
                cnt += freq[idx]
                if cnt >= x:
                    return -(idx + 1)
            return 0
        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            res[i] = get_beauty()
            if i + k < n:
                out = nums[i]
                if out < 0:
                    freq[-out - 1] -= 1
                    neg_count -= 1
                inn = nums[i + k]
                if inn < 0:
                    freq[-inn - 1] += 1
                    neg_count += 1
        return res
