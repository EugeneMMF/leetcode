class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        n = len(grades)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + grades[i]
        i = 0
        group_size = 1
        prev_sum = 0
        count = 0
        while i + group_size <= n:
            curr_sum = pref[i + group_size] - pref[i]
            if curr_sum > prev_sum:
                count += 1
                prev_sum = curr_sum
                i += group_size
                group_size += 1
            else:
                break
        return count