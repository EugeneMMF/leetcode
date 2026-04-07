class Solution:
    def circularPermutation(self, n: int, start: int) -> list[int]:
        num_elements = 1 << n

        gray_code_sequence = []
        for i in range(num_elements):
            gray_code_sequence.append(i ^ (i >> 1))
        
        result_permutation = [gc_val ^ start for gc_val in gray_code_sequence]
        
        return result_permutation
