class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)
        def parse_expr(i):
            res = {""}
            while i < n and expression[i] not in '},':
                term_set, i = parse_term(i)
                new_res = set()
                for a in res:
                    for b in term_set:
                        new_res.add(a + b)
                res = new_res
            return res, i
        def parse_term(i):
            if expression[i] == '{':
                i += 1
                set_union, i = parse_union(i)
                i += 1
                return set_union, i
            else:
                return {expression[i]}, i + 1
        def parse_union(i):
            first_set, i = parse_expr(i)
            total = set(first_set)
            while i < n and expression[i] == ',':
                i += 1
                next_set, i = parse_expr(i)
                total |= next_set
            return total, i
        result, _ = parse_expr(0)
        return sorted(result)
