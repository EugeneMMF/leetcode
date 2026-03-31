class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        # points_diff[k] stores the change in score when transitioning from k-1 to k.
        # It's a difference array used for efficient calculation of scores.
        # We need size n+1 to handle the potential decrement at index n.
        points_diff = [0] * (n + 1)

        for j in range(n):
            # For each original element nums[j] at its initial index j,
            # we determine the ranges of k for which it contributes a point.
            # An element nums[j] contributes a point if its new index 'i'
            # (after rotation by k) satisfies nums[j] <= i.
            # The new index 'i' is given by (j - k + n) % n.
            # So the condition is: nums[j] <= (j - k + n) % n.

            # We analyze two cases for k:
            # Case 1: k <= j. The new index is simply j - k.
            #   The condition becomes: nums[j] <= j - k.
            #   Rearranging for k: k <= j - nums[j].
            #   So, for k in the range [0, j - nums[j]], nums[j] contributes a point.
            #   This range is valid only if j - nums[j] >= 0.
            #   If valid, we mark a +1 at the start of the range (k=0)
            #   and a -1 at the point just after the end of the range (k = j - nums[j] + 1).
            if j >= nums[j]:
                points_diff[0] += 1
                points_diff[j - nums[j] + 1] -= 1

            # Case 2: k > j (i.e., k ranges from j+1 to n-1).
            #   The new index wraps around and is j - k + n.
            #   The condition becomes: nums[j] <= j - k + n.
            #   Rearranging for k: k <= j - nums[j] + n.
            #   So, for k in the range [j+1, min(n-1, j - nums[j] + n)], nums[j] contributes a point.
            #   We need to ensure the start_k is less than or equal to the end_k.
            start_k_second_phase = j + 1
            end_k_second_phase = min(n - 1, j - nums[j] + n)

            if start_k_second_phase <= end_k_second_phase:
                points_diff[start_k_second_phase] += 1
                # The decrement applies for the k value immediately after the range ends.
                # Since points_diff has size n+1, points_diff[n] is a valid index.
                points_diff[end_k_second_phase + 1] -= 1

        current_score = 0
        max_score = -1
        best_k = 0

        # Calculate the actual scores for each k from the difference array
        # and find the k that yields the maximum score (smallest k in case of ties).
        for k in range(n):
            current_score += points_diff[k]
            if current_score > max_score:
                max_score = current_score
                best_k = k
            # If current_score == max_score, we stick with the smaller best_k,
            # which is naturally handled by not updating best_k in case of ties.
        
        return best_k

