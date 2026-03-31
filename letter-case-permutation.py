class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []
        n = len(s)

        def backtrack(index, current_chars):
            if index == n:
                res.append("".join(current_chars))
                return

            char = s[index]
            if char.isalpha():
                current_chars.append(char.lower())
                backtrack(index + 1, current_chars)
                current_chars.pop()

                current_chars.append(char.upper())
                backtrack(index + 1, current_chars)
                current_chars.pop()
            else:
                current_chars.append(char)
                backtrack(index + 1, current_chars)
                current_chars.pop()
        
        backtrack(0, [])
        return res
