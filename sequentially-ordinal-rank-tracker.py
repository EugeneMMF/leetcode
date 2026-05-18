class SORTracker:

    def __init__(self):
        import bisect
        self.bisect = bisect
        self.data = []
        self.get_count = 0

    def add(self, name: str, score: int) -> None:
        key = (-score, name)
        self.bisect.insort(self.data, key)

    def get(self) -> str:
        self.get_count += 1
        return self.data[self.get_count - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()