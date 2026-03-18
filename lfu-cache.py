import collections

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = collections.defaultdict(collections.OrderedDict)
        self.min_freq = 0

    def _update_frequency(self, key: int):
        old_freq = self.key_to_freq[key]
        new_freq = old_freq + 1

        self.key_to_freq[key] = new_freq

        del self.freq_to_keys[old_freq][key]

        if not self.freq_to_keys[old_freq] and old_freq == self.min_freq:
            self.min_freq += 1
        
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self._update_frequency(key)
        
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_frequency(key)
        else:
            if self.size == self.capacity:
                lfu_key = self.freq_to_keys[self.min_freq].popitem(last=False)[0]
                
                del self.key_to_val[lfu_key]
                del self.key_to_freq[lfu_key]
                
                self.size -= 1
                
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            
            self.size += 1
            self.min_freq = 1
            
