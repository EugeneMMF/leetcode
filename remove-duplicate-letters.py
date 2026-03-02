class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue

            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                popped_char = stack.pop()
                visited.remove(popped_char)
            
            stack.append(char)
            visited.add(char)
        
        return "".join(stack)
