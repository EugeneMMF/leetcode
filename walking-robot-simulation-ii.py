class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.dirs = ["East", "North", "West", "South"]
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        # Precompute next state for all states
        self.next_state = {}
        for x in range(self.w):
            for y in range(self.h):
                for d in range(4):
                    nd = d
                    nx = x + self.dx[nd]
                    ny = y + self.dy[nd]
                    while not (0 <= nx < self.w and 0 <= ny < self.h):
                        nd = (nd + 1) % 4
                        nx = x + self.dx[nd]
                        ny = y + self.dy[nd]
                    self.next_state[(x, y, d)] = (nx, ny, nd)
        # Build state sequence and detect cycle
        self.states = []
        self.state_index = {}
        x, y, d = 0, 0, 0  # initial state
        idx = 0
        while True:
            state = (x, y, d)
            if state in self.state_index:
                self.cycle_start = self.state_index[state]
                self.cycle_len = idx - self.cycle_start
                break
            self.state_index[state] = idx
            self.states.append(state)
            idx += 1
            x, y, d = self.next_state[state]
        self.cur_idx = 0

    def step(self, num: int) -> None:
        if self.cur_idx < self.cycle_start:
            if self.cur_idx + num < self.cycle_start:
                self.cur_idx += num
            else:
                rem = self.cur_idx + num - self.cycle_start
                self.cur_idx = self.cycle_start + (rem % self.cycle_len)
        else:
            self.cur_idx = self.cycle_start + ((self.cur_idx - self.cycle_start + num) % self.cycle_len)

    def getPos(self) -> List[int]:
        x, y, _ = self.states[self.cur_idx]
        return [x, y]

    def getDir(self) -> str:
        _, _, d = self.states[self.cur_idx]
        return self.dirs[d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()