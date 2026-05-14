class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        if mx <= total - mx + 1:
            return total
        return 2 * (total - mx) + 1