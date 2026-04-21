class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}
        for i in range(1, n + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            freq[s] = freq.get(s, 0) + 1
        max_sz = max(freq.values())
        return sum(1 for v in freq.values() if v == max_sz)
