class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(st, a, b, gain):
            stack = []
            total = 0
            for ch in st:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    total += gain
                else:
                    stack.append(ch)
            return ''.join(stack), total
        if x >= y:
            s, score1 = remove(s, 'a', 'b', x)
            s, score2 = remove(s, 'b', 'a', y)
        else:
            s, score1 = remove(s, 'b', 'a', y)
            s, score2 = remove(s, 'a', 'b', x)
        return score1 + score2
