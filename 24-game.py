class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        EPSILON = 1e-6

        # Convert initial cards to float for real division
        nums = [float(card) for card in cards]

        def can_make_24(current_nums: list[float]) -> bool:
            # Base case: if only one number is left, check if it's approximately 24
            if len(current_nums) == 1:
                return abs(current_nums[0] - 24) < EPSILON

            n = len(current_nums)
            
            # Iterate through all unique pairs of numbers
            for i in range(n):
                for j in range(i + 1, n):
                    # Pick num1 and num2
                    num1 = current_nums[i]
                    num2 = current_nums[j]

                    # Create a new list containing the numbers not chosen
                    remaining_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            remaining_nums.append(current_nums[k])

                    # Try all 6 possible operations and recurse
                    # Sum
                    if can_make_24(remaining_nums + [num1 + num2]):
                        return True
                    # Difference (num1 - num2)
                    if can_make_24(remaining_nums + [num1 - num2]):
                        return True
                    # Difference (num2 - num1)
                    if can_make_24(remaining_nums + [num2 - num1]):
                        return True
                    # Product
                    if can_make_24(remaining_nums + [num1 * num2]):
                        return True
                    # Division (num1 / num2) - check for division by zero
                    if abs(num2) > EPSILON:
                        if can_make_24(remaining_nums + [num1 / num2]):
                            return True
                    # Division (num2 / num1) - check for division by zero
                    if abs(num1) > EPSILON:
                        if can_make_24(remaining_nums + [num2 / num1]):
                            return True
            
            # If no combination leads to 24, return False
            return False

        return can_make_24(nums)
