import random

class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.sz = n - len(blacklist)
        
        bl_set = set(blacklist)
        
        self.mapping = {}
        
        next_valid_high = self.sz
        
        for b in blacklist:
            if b < self.sz:
                while next_valid_high in bl_set:
                    next_valid_high += 1
                
                self.mapping[b] = next_valid_high
                
                next_valid_high += 1

    def pick(self) -> int:
        r = random.randrange(0, self.sz)
        
        if r in self.mapping:
            return self.mapping[r]
        else:
            return r
