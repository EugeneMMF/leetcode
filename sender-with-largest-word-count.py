import collections
from typing import List

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counts = collections.defaultdict(int)
        for msg, sender in zip(messages, senders):
            counts[sender] += len(msg.split(' '))
        max_words = -1
        best = ""
        for sender, w in counts.items():
            if w > max_words or (w == max_words and sender > best):
                max_words = w
                best = sender
        return best
