class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        if indexDifference == 0:
            if valueDifference == 0:
                return [0, 0]
            min_val = min(nums)
            max_val = max(nums)
            if max_val - min_val >= valueDifference:
                i_min = nums.index(min_val)
                i_max = nums.index(max_val)
                return [i_min, i_max]
            return [-1, -1]
        if valueDifference == 0:
            if indexDifference < n:
                return [0, indexDifference]
            return [-1, -1]
        prefix_min = [0] * n
        prefix_max = [0] * n
        prefix_min_idx = [0] * n
        prefix_max_idx = [0] * n
        prefix_min[0] = nums[0]
        prefix_max[0] = nums[0]
        prefix_min_idx[0] = 0
        prefix_max_idx[0] = 0
        for i in range(1, n):
            if nums[i] < prefix_min[i-1]:
                prefix_min[i] = nums[i]
                prefix_min_idx[i] = i
            else:
                prefix_min[i] = prefix_min[i-1]
                prefix_min_idx[i] = prefix_min_idx[i-1]
            if nums[i] > prefix_max[i-1]:
                prefix_max[i] = nums[i]
                prefix_max_idx[i] = i
            else:
                prefix_max[i] = prefix_max[i-1]
                prefix_max_idx[i] = prefix_max_idx[i-1]
        suffix_min = [0] * n
        suffix_max = [0] * n
        suffix_min_idx = [0] * n
        suffix_max_idx = [0] * n
        suffix_min[n-1] = nums[n-1]
        suffix_max[n-1] = nums[n-1]
        suffix_min_idx[n-1] = n-1
        suffix_max_idx[n-1] = n-1
        for i in range(n-2, -1, -1):
            if nums[i] < suffix_min[i+1]:
                suffix_min[i] = nums[i]
                suffix_min_idx[i] = i
            else:
                suffix_min[i] = suffix_min[i+1]
                suffix_min_idx[i] = suffix_min_idx[i+1]
            if nums[i] > suffix_max[i+1]:
                suffix_max[i] = nums[i]
                suffix_max_idx[i] = i
            else:
                suffix_max[i] = suffix_max[i+1]
                suffix_max_idx[i] = suffix_max_idx[i+1]
        k = indexDifference
        for i in range(n):
            if i - k >= 0:
                if prefix_max[i-k] - nums[i] >= valueDifference:
                    return [i, prefix_max_idx[i-k]]
                if nums[i] - prefix_min[i-k] >= valueDifference:
                    return [i, prefix_min_idx[i-k]]
            if i + k < n:
                if suffix_max[i+k] - nums[i] >= valueDifference:
                    return [i, suffix_max_idx[i+k]]
                if nums[i] - suffix_min[i+k] >= valueDifference:
                    return [i, suffix_min_idx[i+k]]
        return [-1, -1]