class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        c = Counter(text)
        return min(c.get('b', 0), c.get('a', 0), c.get('l', 0) // 2, c.get('o', 0) // 2, c.get('n', 0))
