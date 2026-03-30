class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for num in range(left, right + 1):
            is_self_dividing = True
            temp_num = num
            while temp_num > 0:
                digit = temp_num % 10
                if digit == 0:
                    is_self_dividing = False
                    break
                if num % digit != 0:
                    is_self_dividing = False
                    break
                temp_num //= 10
            if is_self_dividing:
                result.append(num)
        return result
