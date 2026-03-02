from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def _get_max_subsequence(nums, length):
            if length == 0:
                return []
            
            stack = []
            drop = len(nums) - length

            for num in nums:
                while stack and stack[-1] < num and drop > 0:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            
            return stack[:length]

        def _merge_arrays(arr1, arr2):
            res = []
            p1 = 0
            p2 = 0

            def _compare_subarrays(arr1, p1, arr2, p2):
                len1 = len(arr1)
                len2 = len(arr2)
                
                while p1 < len1 and p2 < len2:
                    if arr1[p1] > arr2[p2]:
                        return True
                    if arr1[p1] < arr2[p2]:
                        return False
                    p1 += 1
                    p2 += 1
                
                return p1 < len1

            while p1 < len(arr1) or p2 < len(arr2):
                if _compare_subarrays(arr1, p1, arr2, p2):
                    res.append(arr1[p1])
                    p1 += 1
                else:
                    res.append(arr2[p2])
                    p2 += 1
            return res

        m, n = len(nums1), len(nums2)
        max_num = []

        for i in range(max(0, k - n), min(k, m) + 1):
            subsequence1 = _get_max_subsequence(nums1, i)
            subsequence2 = _get_max_subsequence(nums2, k - i)
            
            merged_num = _merge_arrays(subsequence1, subsequence2)
            
            if merged_num > max_num:
                max_num = merged_num
        
        return max_num