import collections

class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.stacks_by_freq = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        current_freq = self.freq[val]
        self.max_freq = max(self.max_freq, current_freq)
        self.stacks_by_freq[current_freq].append(val)

    def pop(self) -> int:
        val = self.stacks_by_freq[self.max_freq].pop()
        
        self.freq[val] -= 1
        
        if not self.stacks_by_freq[self.max_freq]:
            self.max_freq -= 1

        return val
