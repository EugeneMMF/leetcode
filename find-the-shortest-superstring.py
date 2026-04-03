class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        n = len(words)

        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break

        dp = [[float('inf')] * n for _ in range(1 << n)]
        
        parent = [[-1] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = len(words[i])

        for mask in range(1, 1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue

                prev_mask = mask ^ (1 << i)
                
                for j in range(n):
                    if j == i:
                        continue
                    if not (prev_mask & (1 << j)):
                        continue

                    current_length = dp[prev_mask][j] + len(words[i]) - overlap[j][i]

                    if current_length < dp[mask][i]:
                        dp[mask][i] = current_length
                        parent[mask][i] = j

        min_len = float('inf')
        last_word_idx = -1
        full_mask = (1 << n) - 1

        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last_word_idx = i

        path = []
        current_mask = full_mask
        current_word_idx = last_word_idx

        while current_word_idx != -1:
            path.append(current_word_idx)
            prev_word_idx = parent[current_mask][current_word_idx]
            current_mask ^= (1 << current_word_idx)
            current_word_idx = prev_word_idx

        path.reverse()

        res = words[path[0]]
        for k in range(1, n):
            prev_idx = path[k-1]
            curr_idx = path[k]
            res += words[curr_idx][overlap[prev_idx][curr_idx]:]
            
        return res
