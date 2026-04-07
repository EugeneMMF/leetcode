class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        digits.sort()

        total_sum = sum(digits)
        mod1 = [d for d in digits if d % 3 == 1]
        mod2 = [d for d in digits if d % 3 == 2]

        digits_to_remove = []

        if total_sum % 3 == 1:
            if len(mod1) >= 1:
                digits_to_remove.append(mod1[0])
            elif len(mod2) >= 2:
                digits_to_remove.append(mod2[0])
                digits_to_remove.append(mod2[1])
        elif total_sum % 3 == 2:
            if len(mod2) >= 1:
                digits_to_remove.append(mod2[0])
            elif len(mod1) >= 2:
                digits_to_remove.append(mod1[0])
                digits_to_remove.append(mod1[1])

        temp_digits = list(digits)
        for d_rem in digits_to_remove:
            temp_digits.remove(d_rem)
        final_digits = temp_digits

        final_digits.sort(reverse=True)

        if not final_digits:
            return ""
        if final_digits[0] == 0:
            return "0"

        return "".join(map(str, final_digits))

