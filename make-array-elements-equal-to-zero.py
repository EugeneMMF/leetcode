class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = [i for i, v in enumerate(nums) if v == 0]
        def simulate(start, direction):
            arr = nums[:]
            curr = start
            dir = direction
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir = -dir
                    curr += dir
            return all(v == 0 for v in arr)
        count = 0
        for z in zeros:
            for d in (-1, 1):
                if simulate(z, d):
                    count += 1
        return count
