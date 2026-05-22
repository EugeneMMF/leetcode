class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index('+')
        num1 = expression[:plus]
        num2 = expression[plus+1:]
        best_val = None
        best_str = None
        for i in range(len(num1)+1):
            A = num1[:i]
            B = num1[i:]
            if not B:
                continue
            left = int(A) if A else 1
            for j in range(1, len(num2)+1):
                C = num2[:j]
                D = num2[j:]
                right = int(D) if D else 1
                mid_sum = int(B)+int(C)
                val = left*mid_sum*right
                if best_val is None or val<best_val:
                    best_val = val
                    if A:
                        s = A + '(' + B + '+' + C + ')'
                    else:
                        s = '(' + B + '+' + C + ')'
                    if D:
                        s += D
                    best_str = s
        return best_str