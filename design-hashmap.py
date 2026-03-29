class MyHashMap:

    def __init__(self):
        # The maximum possible key value is 10^6.
        # We can use a direct addressing table (a list) where the index
        # corresponds to the key.
        # Initialize all entries to -1 to signify that no value is mapped to that key.
        self._data = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        # For a given key, directly store the value at the corresponding index.
        self._data[key] = value

    def get(self, key: int) -> int:
        # Retrieve the value stored at the index corresponding to the key.
        # If the value is -1, it means the key is not present.
        return self._data[key]

    def remove(self, key: int) -> None:
        # To remove a key, set its corresponding value back to -1,
        # indicating that no mapping exists for this key.
        self._data[key] = -1

