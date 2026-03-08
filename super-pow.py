class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        # Helper function for (base^exp) % MOD
        def pow_mod(base, exp):
            return pow(base, exp, MOD)

        ans = 1
        
        # Reduce 'a' modulo MOD at the start to keep numbers smaller
        # (a^b) % M is equivalent to ((a % M)^b) % M
        a %= MOD

        # Iterate through the digits of b from left to right
        # The exponent b can be written as (...(b[0] * 10 + b[1]) * 10 + ... + b[k-1])
        # So, a^b = a^(...((b[0]*10 + b[1])*10 + ...) + b[k-1])
        # Using the property: x^(y*10 + z) = (x^y)^10 * x^z
        # We can update the result iteratively.
        for digit in b:
            # Current ans holds a^(processed_prefix_of_b) % MOD
            # To incorporate the new digit 'd', the exponent becomes (processed_prefix_of_b * 10 + d)
            # So, the new result is ( (a^(processed_prefix_of_b))^10 * (a^d) ) % MOD
            ans = (pow_mod(ans, 10) * pow_mod(a, digit)) % MOD
        
        return ans
