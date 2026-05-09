class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict
        user_minutes = defaultdict(set)
        for uid, time in logs:
            user_minutes[uid].add(time)
        counts = [len(minutes) for minutes in user_minutes.values()]
        ans = [0] * (k + 1)
        for c in counts:
            if c <= k:
                ans[c] += 1
        return ans[1:]
