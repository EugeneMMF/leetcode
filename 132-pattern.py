
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        # stack stores potential nums[j] values (the '3' in 132 pattern) in decreasing order.
        # These are candidates for the middle element in terms of index, but largest in terms of value.
        stack = []

        # This variable stores nums[k] (the '2' in 132 pattern).
        # It's initialized to negative infinity because nums[k] must be greater than nums[i].
        # It represents the largest '2' value found so far that has a '3' (larger value) to its right.
        nums_k_val = -float('inf')

        # Iterate from right to left.
        # `i` in this loop refers to the index of `nums[i]` (the '1' in 132 pattern).
        for i in range(n - 1, -1, -1):
            current_num = nums[i]

            # If current_num (which is nums[i]) is less than nums_k_val (which is nums[k]):
            # We have found a 132 pattern.
            #   - `current_num` serves as `nums[i]` (the '1' value).
            #   - `nums_k_val` serves as `nums[k]` (the '2' value).
            #   - The element that caused `nums_k_val` to be set (popped from stack) serves as `nums[j]` (the '3' value).
            #
            # Value conditions:
            # `current_num < nums_k_val` is true by this check.
            # `nums_k_val` was assigned from an element `X` popped from the stack because some
            # larger element `Y` (which is `nums[j]`) was encountered. So, `X < Y`.
            # Thus, `nums_k_val < nums[j]`.
            # Combining these, `nums[i] < nums[k] < nums[j]` is satisfied.
            #
            # Index conditions (i < j < k):
            # Let `idx_i` be the current loop index `i`.
            # Let `idx_k` be the original index of `nums_k_val` in `nums`.
            # Let `idx_j` be the original index of `nums[j]` in `nums`.
            #
            # In our right-to-left scan:
            # - `nums[j]` (at `idx_j`) was processed earlier (further to the right) than `nums_k_val` (at `idx_k`). So, `idx_j > idx_k`.
            # - `nums_k_val` (at `idx_k`) was processed earlier (further to the right) than `current_num` (at `idx_i`). So, `idx_k > idx_i`.
            #
            # Combining these, we get: `idx_j > idx_k > idx_i`.
            # Rearranging to `idx_i < idx_k < idx_j`.
            # This precisely matches the required `i < j < k` indices for the problem definition.
            if current_num < nums_k_val:
                return True

            # If current_num is not nums[i] (the '1') for current nums_k_val, it might be a new nums[j] (the '3').
            # We pop elements from the stack that are smaller than current_num.
            # These popped elements are candidates for nums[k] (the '2').
            # We update nums_k_val to be the maximum of these popped values.
            # This means `nums_k_val` holds the largest `k` (the '2') that has been "released" by a larger `j` (current_num).
            while stack and current_num > stack[-1]: # stack[-1] is peek
                nums_k_val = max(nums_k_val, stack.pop())

            # Push current_num onto the stack. It's a potential nums[j] (the '3').
            # The stack maintains elements in decreasing order.
            stack.append(current_num)

        return False

