class Solution:
    def maxLength(self, arr: list[str]) -> int:
        
        candidate_masks = []
        for s in arr:
            mask = 0
            has_duplicates = False
            for char_code in map(ord, s):
                bit = 1 << (char_code - ord('a'))
                if (mask & bit) != 0:
                    has_duplicates = True
                    break
                mask |= bit
            if not has_duplicates:
                candidate_masks.append((mask, len(s)))

        self.max_len = 0

        def backtrack(index, current_mask, current_length):
            self.max_len = max(self.max_len, current_length)

            if index == len(candidate_masks):
                return

            backtrack(index + 1, current_mask, current_length)

            word_mask, word_len = candidate_masks[index]

            if (word_mask & current_mask) == 0:
                backtrack(index + 1, current_mask | word_mask, current_length + word_len)

        backtrack(0, 0, 0)

        return self.max_len
