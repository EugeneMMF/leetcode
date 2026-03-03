class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        def merge_sort_and_count(arr, low, high):
            if low == high:
                return 0
            
            mid = (low + high) // 2
            
            count = merge_sort_and_count(arr, low, mid) + \
                    merge_sort_and_count(arr, mid + 1, high)
            
            j = low
            k = low
            
            for i_right in range(mid + 1, high + 1):
                while j <= mid and arr[j] < arr[i_right] - upper:
                    j += 1
                
                while k <= mid and arr[k] <= arr[i_right] - lower:
                    k += 1
                
                count += (k - j)
            
            temp = [0] * (high - low + 1)
            ptr1 = low
            ptr2 = mid + 1
            idx = 0
            
            while ptr1 <= mid and ptr2 <= high:
                if arr[ptr1] <= arr[ptr2]:
                    temp[idx] = arr[ptr1]
                    ptr1 += 1
                else:
                    temp[idx] = arr[ptr2]
                    ptr2 += 1
                idx += 1
            
            while ptr1 <= mid:
                temp[idx] = arr[ptr1]
                ptr1 += 1
                idx += 1
            
            while ptr2 <= high:
                temp[idx] = arr[ptr2]
                ptr2 += 1
                idx += 1
                
            for l in range(len(temp)):
                arr[low + l] = temp[l]
            
            return count

        return merge_sort_and_count(prefix_sums, 0, n)
