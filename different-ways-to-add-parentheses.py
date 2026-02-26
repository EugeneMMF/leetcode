class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def calculate(sub_expression: str) -> list[int]:
            if sub_expression in memo:
                return memo[sub_expression]

            results = []
            
            found_operator = False 

            for i, char in enumerate(sub_expression):
                if char in "+-*":
                    found_operator = True
                    left_part = sub_expression[:i]
                    right_part = sub_expression[i+1:]

                    left_results = calculate(left_part)
                    right_results = calculate(right_part)

                    for l_val in left_results:
                        for r_val in right_results:
                            if char == '+':
                                results.append(l_val + r_val)
                            elif char == '-':
                                results.append(l_val - r_val)
                            elif char == '*':
                                results.append(l_val * r_val)
            
            if not found_operator:
                results.append(int(sub_expression))
            
            memo[sub_expression] = results
            return results

        return calculate(expression)
