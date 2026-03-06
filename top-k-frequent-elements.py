import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = collections.Counter(nums)

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
