from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_freq = 0
        for char, freq in counts.items():
            max_freq = max(max_freq, freq)
        
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(heap)
        
        result = []
        prev_freq, prev_char = 0, ''
        
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
            freq += 1
            
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char
            
        return "".join(result)

