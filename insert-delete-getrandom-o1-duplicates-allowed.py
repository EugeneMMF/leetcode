import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.val_to_indices = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        val_present = (len(self.val_to_indices[val]) > 0)
        
        self.val_to_indices[val].add(len(self.nums))
        self.nums.append(val)
        
        return not val_present
        

    def remove(self, val: int) -> bool:
        if not self.val_to_indices[val]:
            return False
        
        idx_to_remove = self.val_to_indices[val].pop()
        
        last_element = self.nums[-1]
        last_index = len(self.nums) - 1
        
        if idx_to_remove != last_index:
            self.nums[idx_to_remove] = last_element
            
            self.val_to_indices[last_element].remove(last_index)
            self.val_to_indices[last_element].add(idx_to_remove)
        
        self.nums.pop()
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)

