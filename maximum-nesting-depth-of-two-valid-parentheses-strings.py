class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        answer = [0] * n
        current_depth = 0

        for i in range(n):
            if seq[i] == '(':
                answer[i] = current_depth % 2
                current_depth += 1
            elif seq[i] == ')':
                current_depth -= 1
                answer[i] = current_depth % 2
        
        return answer
