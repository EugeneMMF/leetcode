class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = [0] * 24
        for h in hours:
            freq[h % 24] += 1
        count = 0
        for r in range(1, 12):
            count += freq[r] * freq[24 - r]
        count += freq[0] * (freq[0] - 1) // 2
        count += freq[12] * (freq[12] - 1) // 2
        return count
