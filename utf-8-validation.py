class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        bytes_to_follow = 0

        for byte_val in data:
            if bytes_to_follow == 0:
                if (byte_val >> 7) == 0:
                    bytes_to_follow = 0
                elif (byte_val >> 5) == 0b110:
                    bytes_to_follow = 1
                elif (byte_val >> 4) == 0b1110:
                    bytes_to_follow = 2
                elif (byte_val >> 3) == 0b11110:
                    bytes_to_follow = 3
                else:
                    return False
            else:
                if (byte_val >> 6) == 0b10:
                    bytes_to_follow -= 1
                else:
                    return False

        return bytes_to_follow == 0