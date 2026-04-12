class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False
        diffs = []
        for i, (a, b) in enumerate(zip(s, goal)):
            if a != b:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        if len(diffs) != 2:
            return False
        i, j = diffs
        return s[i] == goal[j] and s[j] == goal[i]
