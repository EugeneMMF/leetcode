class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        def merge_sort(arr, low, high):
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            
            count = merge_sort(arr, low, mid)
            count += merge_sort(arr, mid + 1, high)
            count += merge(arr, low, mid, high)
            
            return count
        
        def merge(arr, low, mid, high):
            pairs = 0
            
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                pairs += (j - (mid + 1))
            
            temp = []
            p1 = low
            p2 = mid + 1
            
            while p1 <= mid and p2 <= high:
                if arr[p1] <= arr[p2]:
                    temp.append(arr[p1])
                    p1 += 1
                else:
                    temp.append(arr[p2])
                    p2 += 1
            
            while p1 <= mid:
                temp.append(arr[p1])
                p1 += 1
                
            while p2 <= high:
                temp.append(arr[p2])
                p2 += 1
                
            for k in range(len(temp)):
                arr[low + k] = temp[k]
                
            return pairs
        
        return merge_sort(nums, 0, len(nums) - 1)
