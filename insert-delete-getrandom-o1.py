import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.vals.append(val)
        self.indices[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx_to_remove = self.indices[val]
        last_val = self.vals[-1]
        
        self.vals[idx_to_remove] = last_val
        self.indices[last_val] = idx_to_remove
        
        self.vals.pop()
        del self.indices[val]
        
        return True

    def getRandom(self) -> int:
        random_index = random.randrange(len(self.vals))
        return self.vals[random_index]
