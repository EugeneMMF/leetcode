import itertools

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        latest_time = ""

        for p in itertools.permutations(arr):
            h1, h2, m1, m2 = p
            
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                current_time_str = f"{hours:02}:{minutes:02}"

                if not latest_time or current_time_str > latest_time:
                    latest_time = current_time_str
        
        return latest_time
