class Solution:
    def rankTeams(self, votes):
        m = len(votes[0])
        cnt = {c: [0] * m for c in votes[0]}
        for v in votes:
            for i, ch in enumerate(v):
                cnt[ch][i] += 1
        teams = sorted(cnt.keys(), key=lambda t: tuple([-cnt[t][i] for i in range(m)]) + (t,))
        return ''.join(teams)
