class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + tiles[i][1] - tiles[i][0] + 1
        max_cover = 0
        right = 0
        for left in range(n):
            end = tiles[left][0] + carpetLen - 1
            while right < n and tiles[right][0] <= end:
                right += 1
            total = pref[right] - pref[left]
            last = right - 1
            if end < tiles[last][1]:
                total -= tiles[last][1] - end
            if total > max_cover:
                max_cover = total
        return max_cover