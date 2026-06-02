class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        whites = sum(1 for i in range(k) if blocks[i] == 'W')
        min_whites = whites
        for i in range(k, n):
            if blocks[i - k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            if whites < min_whites:
                min_whites = whites
        return min_whites
