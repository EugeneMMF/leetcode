class Solution:
    def robotSim(self, commands, obstacles):
        obs = { (x, y) for x, y in obstacles }
        x = y = 0
        dir = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        maxd = 0
        for c in commands:
            if c == -2:
                dir = (dir + 3) % 4
            elif c == -1:
                dir = (dir + 1) % 4
            else:
                dx, dy = dirs[dir]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    d = x*x + y*y
                    if d > maxd:
                        maxd = d
        return maxd
