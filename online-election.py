from typing import List
import bisect

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        cnt = {}
        lead = -1
        max_votes = 0
        for p in persons:
            cnt[p] = cnt.get(p, 0) + 1
            if cnt[p] >= max_votes:
                lead = p
                max_votes = cnt[p]
            self.leaders.append(lead)

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t) - 1
        return self.leaders[i]
