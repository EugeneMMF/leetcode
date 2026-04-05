class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def _eval(idx: int) -> tuple[bool, int]:
            char = expression[idx]

            if char == 't':
                return True, idx + 1
            elif char == 'f':
                return False, idx + 1
            elif char == '!':
                sub_expr_val, next_idx_after_sub_expr = _eval(idx + 2)
                return not sub_expr_val, next_idx_after_sub_expr + 1
            elif char == '&' or char == '|':
                op_char = char
                values = []
                
                current_idx = idx + 2
                
                while True:
                    sub_expr_val, next_idx_after_sub_expr = _eval(current_idx)
                    values.append(sub_expr_val)
                    current_idx = next_idx_after_sub_expr
                    
                    if expression[current_idx] == ')':
                        break 
                    elif expression[current_idx] == ',':
                        current_idx += 1 
                
                if op_char == '&':
                    result = True
                    for val in values:
                        if not val:
                            result = False
                            break
                    return result, current_idx + 1 
                else: 
                    result = False
                    for val in values:
                        if val:
                            result = True
                            break
                    return result, current_idx + 1 
            
            return False, -1 

        final_result, _ = _eval(0)
        return final_result
