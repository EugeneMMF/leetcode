class MyHashSet:

    def __init__(self):
        self._data = [False] * 1000001

    def add(self, key: int) -> None:
        self._data[key] = True

    def remove(self, key: int) -> None:
        self._data[key] = False

    def contains(self, key: int) -> bool:
        return self._data[key]
