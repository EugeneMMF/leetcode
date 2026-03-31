class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if not s:
            return True
        
        temp = s + s
        return goal in temp
