class Solution:
    def maxJump(self, stones):
        n=len(stones)
        max_consecutive=0
        for i in range(n-1):
            diff=stones[i+1]-stones[i]
            if diff>max_consecutive:
                max_consecutive=diff
        max_two_step=0
        for i in range(n-2):
            diff=stones[i+2]-stones[i]
            if diff>max_two_step:
                max_two_step=diff
        return max(max_consecutive,max_two_step)