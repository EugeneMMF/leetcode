import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        n = len(formula)
        self.i = 0

        def parse_number():
            start_i = self.i
            num = 0
            while self.i < n and formula[self.i].isdigit():
                num = num * 10 + int(formula[self.i])
                self.i += 1
            return num if start_i < self.i else 1

        stack = [collections.Counter()]

        while self.i < n:
            if formula[self.i] == '(':
                stack.append(collections.Counter())
                self.i += 1
            elif formula[self.i] == ')':
                current_counts = stack.pop()
                self.i += 1
                multiplier = parse_number()
                for atom, count in current_counts.items():
                    stack[-1][atom] += count * multiplier
            else:
                start_atom_idx = self.i
                self.i += 1
                while self.i < n and formula[self.i].islower():
                    self.i += 1
                atom_name = formula[start_atom_idx:self.i]

                atom_count = parse_number()
                
                stack[-1][atom_name] += atom_count
        
        final_counts = stack[0]

        sorted_elements = sorted(final_counts.items())

        result_string_parts = []
        for atom, count in sorted_elements:
            result_string_parts.append(atom)
            if count > 1:
                result_string_parts.append(str(count))
        
        return "".join(result_string_parts)
