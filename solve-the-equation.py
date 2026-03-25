
class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def evaluate_side(s: str) -> tuple[int, int]:
            x_coeff = 0
            const_val = 0
            i = 0
            n = len(s)

            while i < n:
                sign = 1
                
                if s[i] == '+':
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1

                start_term_num = i
                while i < n and s[i].isdigit():
                    i += 1
                
                if i < n and s[i] == 'x':
                    if start_term_num == i:
                        num_val = 1
                    else:
                        num_val = int(s[start_term_num:i])
                    x_coeff += sign * num_val
                    i += 1
                else:
                    num_val = int(s[start_term_num:i])
                    const_val += sign * num_val
            
            return x_coeff, const_val
        
        
        left_expr, right_expr = equation.split('=')
        
        left_x_coeff, left_const_val = evaluate_side(left_expr)
        right_x_coeff, right_const_val = evaluate_side(right_expr)
        
        a = left_x_coeff - right_x_coeff
        b = right_const_val - left_const_val
        
        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={b // a}"
