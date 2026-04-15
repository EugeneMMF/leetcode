class TimeMap:
    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ts_list, val_list = self.store[key]
        import bisect
        idx = bisect.bisect_right(ts_list, timestamp) - 1
        return val_list[idx] if idx >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
