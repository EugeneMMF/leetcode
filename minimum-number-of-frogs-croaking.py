class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        order = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cnt = [0] * 5
        max_frogs = 0
        for ch in croakOfFrogs:
            idx = order[ch]
            if idx == 0:
                cnt[0] += 1
            else:
                if cnt[idx - 1] == 0:
                    return -1
                cnt[idx - 1] -= 1
                cnt[idx] += 1
            if ch == 'k':
                cnt[4] -= 1
            max_frogs = max(max_frogs, sum(cnt[:4]))
        if any(cnt[:4]):
            return -1
        return max_frogs
