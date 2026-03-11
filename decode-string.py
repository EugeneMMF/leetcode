class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if '0' <= char <= '9':
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current accumulated number and string onto their respective stacks
                # This signifies entering a new level of decoding
                num_stack.append(current_num)
                str_stack.append(current_str)
                # Reset for the new segment inside brackets
                current_num = 0
                current_str = ""
            elif char == ']':
                # Pop the last number and string from stacks
                prev_num = num_stack.pop()
                prev_str = str_stack.pop()
                # Repeat the current_str (which is the content of the brackets)
                # and append it to the string that was accumulated before this bracket
                current_str = prev_str + current_str * prev_num
            else: # char is a lowercase English letter
                current_str += char
        
        return current_str
