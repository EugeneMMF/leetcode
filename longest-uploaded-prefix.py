class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.visited = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.visited[video] = True
        while self.prefix < self.n and self.visited[self.prefix + 1]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
