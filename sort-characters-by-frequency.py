import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = collections.Counter(s)
        sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
        return "".join(result)
