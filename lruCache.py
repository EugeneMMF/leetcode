class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache:dict[int, tuple[int,int]] = {} # value is a tuple of (value, accessIndex)
    self.accessDict:dict[int,int] = {} # key is accessIndex, value is the key of the item in cache
    self.currentCapacity = 0
    self.evictIndex = 0
    self.accessCounter = 0

  def get(self, key: int) -> int:
    if value := self.cache.get(key, None):
      self.cache[key] = (value[0], self.accessCounter)
      self.accessDict.pop(value[1])
      self.accessDict[self.accessCounter] = key
      self.accessCounter += 1
      return value[0]
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if not self.cache.get(key, None):
      self.currentCapacity += 1
      if self.currentCapacity > self.capacity:
        while self.evictIndex not in self.accessDict:
          self.evictIndex += 1
        keyToRemove = self.accessDict[self.evictIndex]
        self.accessDict.pop(self.evictIndex)
        self.cache.pop(keyToRemove)
    else:
      self.accessDict.pop(self.cache[key][1])
    self.cache[key] = (value, self.accessCounter)
    self.accessDict[self.accessCounter] = key
    self.accessCounter += 1


# Your LRUCache object will be instantiated and called as such:
capacity = 2
operations = ["LRUCache","put","put","put","put","get","get"]
params = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
cache = None
for operation,param in zip(operations, params):
  print("#"*20)
  print(f"{operation=} with {param=}")
  if operation == "LRUCache":
    cache = LRUCache(param[0])
    print(str(None))
  elif operation == "put":
    print(str(cache.put(param[0], param[1])))
  else:
    print(f"{cache.get(param[0])}")