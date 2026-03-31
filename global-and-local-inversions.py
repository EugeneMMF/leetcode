class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        n = len(nums)
        
        # `min_val_for_check` will store min(nums[k] for k in range(i+2, n)) for the current `i`.
        # `min_val_for_update` will store min(nums[k] for k in range(i+1, n)) for the current `i`.
        # These are updated in each iteration `i` to reflect the values needed for the next iteration `i-1`.
        
        # Initialize as if we have processed `n-1` and `n-2` indices,
        # so for `i = n-1` or `i = n-2`, `min(nums[k] for k in range(i+2, n))` is effectively `infinity`.
        min_val_for_check = float('inf')
        min_val_for_update = float('inf')

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            # The check `nums[i] > min_val_for_check` needs to be performed when `i+2` is a valid index,
            # meaning `i <= n - 3`.
            if i <= n - 3:
                if nums[i] > min_val_for_check:
                    return False
            
            # Update `min_val_for_check` and `min_val_for_update` for the next iteration (`i-1`).
            # For `i-1`, the new `min_val_for_check` will be the current `min_val_for_update` (which covers `nums[i+1]` onwards).
            # The new `min_val_for_update` for `i-1` will be `min(nums[i], current_min_val_for_update)`.
            
            min_val_for_check = min_val_for_update
            min_val_for_update = min(min_val_for_update, nums[i])
        
        return True

