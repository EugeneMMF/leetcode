class Solution:
    def numFriendRequests(self, ages):
        freq = [0] * 121
        for age in ages:
            freq[age] += 1
        pref = [0] * 121
        running = 0
        for i in range(121):
            running += freq[i]
            pref[i] = running
        total = 0
        for a in range(15, 121):
            if freq[a] == 0:
                continue
            low = a // 2 + 8
            if low > a:
                continue
            cnt = pref[a] - (pref[low - 1] if low > 0 else 0)
            total += freq[a] * cnt - freq[a]
        return total
