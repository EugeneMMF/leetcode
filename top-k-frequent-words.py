from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        
        heap = []
        for word, freq in word_counts.items():
            heapq.heappush(heap, (-freq, word))
            
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result

