class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_q = []
        dire_q = []

        for i, party in enumerate(senate):
            if party == 'R':
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while radiant_q and dire_q:
            r_idx = radiant_q.pop(0)
            d_idx = dire_q.pop(0)

            if r_idx < d_idx:
                radiant_q.append(r_idx + n)
            else:
                dire_q.append(d_idx + n)

        return "Radiant" if radiant_q else "Dire"

