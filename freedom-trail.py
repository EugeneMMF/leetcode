import collections

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        M = len(key)

        char_indices = collections.defaultdict(list)
        for i, char in enumerate(ring):
            char_indices[char].append(i)

        dp = [collections.defaultdict(lambda: float('inf')) for _ in range(M)]

        first_key_char = key[0]
        for r_pos in char_indices[first_key_char]:
            rotation_cost = min(r_pos, N - r_pos)
            dp[0][r_pos] = rotation_cost + 1

        for k_idx in range(1, M):
            target_char = key[k_idx]
            for prev_r_pos, prev_total_steps in dp[k_idx-1].items():
                for curr_r_pos in char_indices[target_char]:
                    diff = abs(curr_r_pos - prev_r_pos)
                    rotation_cost = min(diff, N - diff)
                    
                    current_total_steps = prev_total_steps + rotation_cost + 1
                    
                    dp[k_idx][curr_r_pos] = min(dp[k_idx][curr_r_pos], current_total_steps)

        return min(dp[M-1].values())
