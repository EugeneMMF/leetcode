class Solution:
    def compress(self, chars: list[str]) -> int:
        read_ptr = 0
        write_ptr = 0
        n = len(chars)

        while read_ptr < n:
            current_char = chars[read_ptr]
            count = 0
            
            while read_ptr < n and chars[read_ptr] == current_char:
                count += 1
                read_ptr += 1
            
            chars[write_ptr] = current_char
            write_ptr += 1
            
            if count > 1:
                for digit_char in str(count):
                    chars[write_ptr] = digit_char
                    write_ptr += 1
        
        return write_ptr
