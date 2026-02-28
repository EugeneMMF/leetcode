
import collections

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        queue = collections.deque([s])
        visited = {s}
        result = []
        found_first_valid_at_level = False

        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                current_s = queue.popleft()

                if is_valid(current_s):
                    result.append(current_s)
                    found_first_valid_at_level = True
                
                if not found_first_valid_at_level:
                    for i in range(len(current_s)):
                        char = current_s[i]
                        
                        if i > 0 and char == current_s[i-1] and (char == '(' or char == ')'):
                            continue

                        if char == '(' or char == ')':
                            next_s = current_s[:i] + current_s[i+1:]
                            if next_s not in visited:
                                visited.add(next_s)
                                queue.append(next_s)
            
            if found_first_valid_at_level:
                return result
        
        return result
