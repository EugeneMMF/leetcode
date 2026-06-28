class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        best_len = 1
        best_end = 0
        for i in range(n):
            wi = words[i]
            li = len(wi)
            gi = groups[i]
            for j in range(i):
                if groups[j] == gi:
                    continue
                if len(words[j]) != li:
                    continue
                diff = 0
                wj = words[j]
                for a, b in zip(wi, wj):
                    if a != b:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i
        seq_indices = []
        cur = best_end
        while cur != -1:
            seq_indices.append(cur)
            cur = prev[cur]
        seq_indices.reverse()
        return [words[i] for i in seq_indices]