class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        visited = set()
        res = []
        
        start_prefix = "0" * (n - 1)
        
        def dfs(current_prefix):
            for digit in range(k - 1, -1, -1):
                char_digit = str(digit)
                next_password_str = current_prefix + char_digit
                
                if next_password_str not in visited:
                    visited.add(next_password_str)
                    dfs(next_password_str[1:])
                    res.append(char_digit)

        dfs(start_prefix)
        
        return start_prefix + "".join(reversed(res))
