class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        n = len(hours)
        
        prefix_sums = [0] * (n + 1)
        current_sum = 0
        for i in range(n):
            score = 1 if hours[i] > 8 else -1
            current_sum += score
            prefix_sums[i+1] = current_sum
        
        stack = []
        for i in range(n + 1):
            if not stack or prefix_sums[i] < prefix_sums[stack[-1]]:
                stack.append(i)
        
        max_length = 0
        for j in range(n, -1, -1):
            while stack and prefix_sums[j] > prefix_sums[stack[-1]]:
                i_from_stack = stack.pop()
                max_length = max(max_length, j - i_from_stack)
        
        return max_length
