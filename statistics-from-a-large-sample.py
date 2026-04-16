from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = 0
        sum_val = 0
        mode = 0
        max_count = -1
        min_val = -1
        max_val = -1
        for i, c in enumerate(count):
            if c:
                if min_val == -1:
                    min_val = i
                max_val = i
                total += c
                sum_val += i * c
                if c > max_count:
                    max_count = c
                    mode = i
        mean = sum_val / total
        if total % 2:
            target = (total + 1) // 2
            cum = 0
            for i, c in enumerate(count):
                cum += c
                if cum >= target:
                    median = i
                    break
        else:
            target1 = total // 2
            target2 = target1 + 1
            cum = 0
            m1 = None
            m2 = None
            for i, c in enumerate(count):
                cum += c
                if m1 is None and cum >= target1:
                    m1 = i
                if m2 is None and cum >= target2:
                    m2 = i
                    break
            median = (m1 + m2) / 2
        return [float(min_val), float(max_val), mean, median, float(mode)]
