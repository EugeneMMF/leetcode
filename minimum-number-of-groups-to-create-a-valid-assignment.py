class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        from collections import Counter
        cnt = Counter(balls)
        min_count = min(cnt.values())
        best = float('inf')
        for x in range(1, min_count + 1):
            total = 0
            ok = True
            for c in cnt.values():
                # check feasibility
                if (c + x) // (x + 1) > c // x:
                    ok = False
                    break
                total += (c + x) // (x + 1)
            if ok and total < best:
                best = total
        return best
