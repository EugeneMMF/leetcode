class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num_str: str):
            parts = num_str.split('+')
            real = int(parts[0])
            imag = int(parts[1][:-1])
            return real, imag

        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)

        result_real = (real1 * real2) - (imag1 * imag2)
        result_imag = (real1 * imag2) + (imag1 * real2)

        return str(result_real) + "+" + str(result_imag) + "i"
