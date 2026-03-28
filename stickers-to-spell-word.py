class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        
        sticker_char_counts = []
        for sticker in stickers:
            counts = [0] * 26
            for char_code in map(ord, sticker):
                counts[char_code - ord('a')] += 1
            sticker_char_counts.append(counts)

        memo = {}
        
        def solve(current_target_counts: tuple) -> int:
            if all(count == 0 for count in current_target_counts):
                return 0

            if current_target_counts in memo:
                return memo[current_target_counts]

            min_stickers_needed = float('inf')

            first_char_idx = -1
            for i in range(26):
                if current_target_counts[i] > 0:
                    first_char_idx = i
                    break
            
            if first_char_idx == -1:
                return 0

            for s_counts in sticker_char_counts:
                if s_counts[first_char_idx] == 0:
                    continue

                next_target_counts_list = list(current_target_counts)
                
                for i in range(26):
                    next_target_counts_list[i] = max(0, next_target_counts_list[i] - s_counts[i])
                
                current_stickers_count = 1 + solve(tuple(next_target_counts_list))
                min_stickers_needed = min(min_stickers_needed, current_stickers_count)

            memo[current_target_counts] = min_stickers_needed
            return min_stickers_needed

        initial_target_counts_list = [0] * 26
        for char_code in map(ord, target):
            initial_target_counts_list[char_code - ord('a')] += 1
        
        initial_target_counts_tuple = tuple(initial_target_counts_list)

        result = solve(initial_target_counts_tuple)

        return result if result != float('inf') else -1
