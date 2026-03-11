
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Handle the edge case for an empty array, though constraints say n >= 1
        if n == 0:
            return 0

        # Calculate the sum of all elements in nums. This sum remains constant across rotations.
        total_sum = sum(nums)

        # Calculate F(0) as the initial rotation function value.
        # F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]
        current_F_val = 0
        for i in range(n):
            current_F_val += i * nums[i]
        
        # Initialize max_F_val with F(0)
        max_F_val = current_F_val

        # Iterate from k=1 to k=n-1 to calculate F(k) values using a recurrence relation.
        # The relation is F(k+1) = F(k) + total_sum - n * arrk[n-1]
        # Where arrk[n-1] is the element that "rotates out" from the last position
        # and moves to the first position (multiplied by 0) in the next rotation.
        # This element is nums[n - 1 - k] when calculating F(k+1) from F(k).
        # In the loop, 'i' represents 'k' in the formula F(k+1) from F(k).
        for i in range(n - 1): # i goes from 0 to n-2, to calculate F(1) through F(n-1)
            # Calculate F(i+1) using F(i)
            # current_F_val (which is F(i)) becomes F(i+1)
            # The element arr_i[n-1] is nums[n - 1 - i].
            current_F_val = current_F_val + total_sum - n * nums[n - 1 - i]
            # Update the maximum F value found so far
            max_F_val = max(max_F_val, current_F_val)
        
        return max_F_val

