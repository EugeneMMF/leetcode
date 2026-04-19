class Solution:
    def isSolvable(self, words, result):
        from collections import defaultdict
        leading = set()
        for w in words:
            if len(w) > 1:
                leading.add(w[0])
        if len(result) > 1:
            leading.add(result[0])
        all_letters = set(''.join(words) + result)
        assign = {ch: -1 for ch in all_letters}
        used = [False] * 10
        words_rev = [w[::-1] for w in words]
        result_rev = result[::-1]
        max_len = max(max(len(w) for w in words), len(result))
        def backtrack(col, carry):
            if col == max_len:
                return carry == 0
            def dfs_word(idx, total):
                if idx == len(words_rev):
                    res_ch = result_rev[col] if col < len(result_rev) else None
                    if res_ch is None:
                        if total % 10 != 0:
                            return False
                        return backtrack(col + 1, total // 10)
                    digit = total % 10
                    if assign[res_ch] != -1:
                        if assign[res_ch] != digit:
                            return False
                        return backtrack(col + 1, total // 10)
                    if used[digit] or (digit == 0 and res_ch in leading):
                        return False
                    assign[res_ch] = digit
                    used[digit] = True
                    if backtrack(col + 1, total // 10):
                        return True
                    assign[res_ch] = -1
                    used[digit] = False
                    return False
                ch = words_rev[idx][col] if col < len(words_rev[idx]) else None
                if ch is None:
                    return dfs_word(idx + 1, total)
                if assign[ch] != -1:
                    return dfs_word(idx + 1, total + assign[ch])
                for d in range(10):
                    if used[d]:
                        continue
                    if d == 0 and ch in leading:
                        continue
                    assign[ch] = d
                    used[d] = True
                    if dfs_word(idx + 1, total + d):
                        return True
                    assign[ch] = -1
                    used[d] = False
                return False
            return dfs_word(0, carry)
        return backtrack(0, 0)
