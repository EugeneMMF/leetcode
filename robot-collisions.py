class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(range(len(positions)), key=lambda i: positions[i])
        stack = []
        survivors = {}
        for i in robots:
            dir = directions[i]
            if dir == 'R':
                stack.append([i, healths[i]])
            else:
                curr_health = healths[i]
                alive = True
                while stack and alive:
                    top_idx, top_health = stack[-1]
                    if top_health > curr_health:
                        stack[-1][1] -= 1
                        alive = False
                    elif top_health < curr_health:
                        stack.pop()
                        curr_health -= 1
                    else:
                        stack.pop()
                        alive = False
                if alive:
                    survivors[i] = curr_health
        for idx, h in stack:
            survivors[idx] = h
        return [survivors[i] for i in range(len(positions)) if i in survivors]
