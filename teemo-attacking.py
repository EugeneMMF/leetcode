class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total_poisoned_time = 0
        n = len(timeSeries)

        if n == 0:
            return 0

        for i in range(n - 1):
            # The time poisoned by the current attack (timeSeries[i]) is either
            # the full duration, or it is cut short by the next attack (timeSeries[i+1]).
            # If the next attack is at timeSeries[i+1], the current poison effect
            # will effectively end at timeSeries[i+1] - 1.
            # So, the duration of the current poison effect before potential reset is
            # (timeSeries[i+1] - 1) - timeSeries[i] + 1 = timeSeries[i+1] - timeSeries[i].
            # We take the minimum of this value and the full duration.
            total_poisoned_time += min(duration, timeSeries[i+1] - timeSeries[i])

        # The last attack always contributes its full duration because there are no subsequent attacks to reset its timer.
        total_poisoned_time += duration

        return total_poisoned_time
