from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            identifier, rest = log.split(' ', 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((rest, identifier, log))
        letters.sort(key=lambda x: (x[0], x[1]))
        return [log for _, _, log in letters] + digits
