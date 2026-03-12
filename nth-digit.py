class Solution:
    def findNthDigit(self, n: int) -> int:
        digits_count = 1
        numbers_in_block = 9
        power_of_10 = 1

        while n > digits_count * numbers_in_block:
            n -= digits_count * numbers_in_block
            digits_count += 1
            numbers_in_block *= 10
            power_of_10 *= 10

        number_index_in_block = (n - 1) // digits_count
        target_num = power_of_10 + number_index_in_block

        digit_index_in_num = (n - 1) % digits_count

        return int(str(target_num)[digit_index_in_num])
