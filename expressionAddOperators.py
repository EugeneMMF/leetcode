class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        results = []
        n = len(num)

        def backtrack(index, current_expression, current_value, prev_operand):
            if index == n:
                if current_value == target:
                    results.append(current_expression)
                return

            for i in range(index, n):
                operand_str = num[index : i + 1]
                if len(operand_str) > 1 and operand_str[0] == '0':
                    break
                operand_val = int(operand_str)

                if index == 0:
                    backtrack(i + 1, operand_str, operand_val, operand_val)
                else:
                    backtrack(i + 1, current_expression + '+' + operand_str, current_value + operand_val, operand_val)
                    backtrack(i + 1, current_expression + '-' + operand_str, current_value - operand_val, -operand_val)
                    backtrack(i + 1, current_expression + '*' + operand_str, (current_value - prev_operand) + (prev_operand * operand_val), prev_operand * operand_val)

        backtrack(0, "", 0, 0)
        return results
