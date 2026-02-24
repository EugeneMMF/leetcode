class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        last_operator = '+' 

        s_extended = s + '+' 

        for char in s_extended:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char.isspace():
                continue 
            else: 
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    operand1 = stack.pop()
                    stack.append(operand1 * current_number)
                elif last_operator == '/':
                    operand1 = stack.pop()
                    
                    res = operand1 // current_number
                    if (operand1 < 0) != (current_number < 0) and operand1 % current_number != 0:
                        res += 1
                    stack.append(res)
                
                last_operator = char
                current_number = 0
        
        return sum(stack)
