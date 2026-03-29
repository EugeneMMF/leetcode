import functools

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False
        
        target_sum_per_subset = total_sum // k
        
        nums.sort(reverse=True)
        
        if nums[0] > target_sum_per_subset:
            return False

        buckets = [0] * k
        
        memo = {}

        def backtrack(index: int) -> bool:
            if index == len(nums):
                return True
            
            canonical_buckets_state = tuple(sorted(buckets))
            
            if (index, canonical_buckets_state) in memo:
                return memo[(index, canonical_buckets_state)]
            
            current_num = nums[index]
            
            for i in range(k):
                if i > 0 and buckets[i] == buckets[i-1]:
                    continue

                if buckets[i] + current_num <= target_sum_per_subset:
                    buckets[i] += current_num
                    
                    if backtrack(index + 1):
                        memo[(index, canonical_buckets_state)] = True
                        return True
                    
                    buckets[i] -= current_num
            
            memo[(index, canonical_buckets_state)] = False
            return False

        return backtrack(0)
