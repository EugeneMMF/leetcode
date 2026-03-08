class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        # Initialize count for the first element
        count = 1
        # prev_diff stores the difference between the last two elements added to the wiggle sequence.
        # 0 means no significant difference has been established yet (e.g., all elements so far are equal, or it's just the first element).
        # Positive means the last segment was an "up" wiggle.
        # Negative means the last segment was a "down" wiggle.
        prev_diff = 0 

        for i in range(1, n):
            current_diff = nums[i] - nums[i-1]

            # If current_diff is positive and previous segment was non-positive (down or flat),
            # it forms a new "up" wiggle.
            if current_diff > 0 and prev_diff <= 0:
                count += 1
                prev_diff = current_diff
            # If current_diff is negative and previous segment was non-negative (up or flat),
            # it forms a new "down" wiggle.
            elif current_diff < 0 and prev_diff >= 0:
                count += 1
                prev_diff = current_diff
            # If current_diff is 0, or if it continues the same trend (e.g., up after up),
            # we don't increment the count. If it's a continuing trend, we effectively replace
            # the intermediate peak/valley with the current element to get a longer overall
            # segment of the same direction. For example, in [1, 5, 10], we effectively take [1, 10].
            # The prev_diff is updated only when a new turning point (wiggle) is found.
            # However, if current_diff has the same sign as prev_diff, prev_diff already holds that sign.
            # So, we only update prev_diff if a new wiggle is found (as per the if/elif conditions).
        
        return count
