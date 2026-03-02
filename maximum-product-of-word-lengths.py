class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        for i in range(n):
            word = words[i]
            current_mask = 0
            for char_code in map(ord, word):
                current_mask |= (1 << (char_code - ord('a')))
            masks[i] = current_mask
            lengths[i] = len(word)

        max_prod = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (masks[i] & masks[j]) == 0:
                    max_prod = max(max_prod, lengths[i] * lengths[j])

        return max_prod
