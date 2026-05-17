class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for s in arr:
            freq[s] = freq.get(s, 0) + 1
        distinct_count = 0
        for s in arr:
            if freq[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""
