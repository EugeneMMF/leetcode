class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        n = len(nums)
        temp = sorted(nums)
        
        mid_idx = (n - 1) // 2
        
        j = mid_idx
        k = n - 1
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = temp[j]
                j -= 1
            else:
                nums[i] = temp[k]
                k -= 1
