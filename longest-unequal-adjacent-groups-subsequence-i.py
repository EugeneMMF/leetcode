class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        best_len = [0, 0]
        best_seq = [[], []]
        for w, g in zip(words, groups):
            opp = 1 - g
            new_len = best_len[opp] + 1
            if new_len > best_len[g]:
                best_len[g] = new_len
                best_seq[g] = best_seq[opp] + [w]
            if best_len[g] == 0:
                best_len[g] = 1
                best_seq[g] = [w]
        return best_seq[0] if best_len[0] >= best_len[1] else best_seq[1]