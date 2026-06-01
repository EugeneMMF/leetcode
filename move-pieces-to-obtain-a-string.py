class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_pos = []
        target_pos = []
        start_chars = []
        target_chars = []
        for i, ch in enumerate(start):
            if ch != '_':
                start_pos.append(i)
                start_chars.append(ch)
        for i, ch in enumerate(target):
            if ch != '_':
                target_pos.append(i)
                target_chars.append(ch)
        if start_chars != target_chars:
            return False
        for s, t, ch in zip(start_pos, target_pos, start_chars):
            if ch == 'L' and s < t:
                return False
            if ch == 'R' and s > t:
                return False
        return True