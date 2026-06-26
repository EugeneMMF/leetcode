class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        seen = {}
        ans = 0
        for x, y in coordinates:
            for dx in range(k + 1):
                dy = k - dx
                px = x ^ dx
                py = y ^ dy
                cnt = seen.get((px, py))
                if cnt:
                    ans += cnt
            seen[(x, y)] = seen.get((x, y), 0) + 1
        return ans
