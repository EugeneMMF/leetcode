class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(num: str):
            if '.' in num:
                int_part, frac_part = num.split('.')
            else:
                int_part, frac_part = num, ''
            if '(' in frac_part:
                nonrep, rep = frac_part.split('(')
                rep = rep.rstrip(')')
            else:
                nonrep, rep = frac_part, ''
            I = int(int_part)
            A = nonrep
            B = rep
            len_a = len(A)
            len_b = len(B)
            if len_b == 0:
                den = 10 ** len_a
                num_val = I * den + (int(A) if A else 0)
            else:
                pow_a = 10 ** len_a
                pow_b = 10 ** len_b
                den = pow_a * (pow_b - 1)
                a_val = int(A) if A else 0
                b_val = int(B)
                num_val = I * den + a_val * (pow_b - 1) + b_val
            return num_val, den
        n1, d1 = parse(s)
        n2, d2 = parse(t)
        return n1 * d2 == n2 * d1
