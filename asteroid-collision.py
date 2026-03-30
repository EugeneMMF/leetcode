class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for new_asteroid in asteroids:
            new_asteroid_destroyed = False
            while stack and new_asteroid < 0 and stack[-1] > 0:
                
                last_asteroid = stack[-1]

                if abs(last_asteroid) == abs(new_asteroid):
                    stack.pop()
                    new_asteroid_destroyed = True
                    break
                elif abs(last_asteroid) > abs(new_asteroid):
                    new_asteroid_destroyed = True
                    break
                else: 
                    stack.pop()
            
            if not new_asteroid_destroyed:
                stack.append(new_asteroid)
        
        return stack
