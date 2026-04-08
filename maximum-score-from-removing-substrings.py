class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calculate_score(string, first_char, second_char, points):
            score = 0
            stack = []
            for char in string:
                if stack and stack[-1] == first_char and char == second_char:
                    score += points
                    stack.pop()
                else:
                    stack.append(char)
            return score, "".join(stack)

        if x > y:
            score1, remaining_s1 = calculate_score(s, 'a', 'b', x)
            score2, _ = calculate_score(remaining_s1, 'b', 'a', y)
            return score1 + score2
        else:
            score1, remaining_s1 = calculate_score(s, 'b', 'a', y)
            score2, _ = calculate_score(remaining_s1, 'a', 'b', x)
            return score1 + score2

