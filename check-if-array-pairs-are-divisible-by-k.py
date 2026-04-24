class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = {}
        for num in arr:
            r = num % k
            freq[r] = freq.get(r, 0) + 1
        for r, cnt in freq.items():
            if r == 0:
                if cnt % 2 != 0:
                    return False
            elif 2 * r == k:
                if cnt % 2 != 0:
                    return False
            else:
                complement = k - r
                if freq.get(complement, 0) != cnt:
                    return False
        return True
