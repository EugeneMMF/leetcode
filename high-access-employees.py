class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        from collections import defaultdict
        times_by_emp = defaultdict(list)
        for name, t in access_times:
            minutes = int(t[:2]) * 60 + int(t[2:])
            times_by_emp[name].append(minutes)
        high = []
        for name, times in times_by_emp.items():
            times.sort()
            n = len(times)
            for i in range(n - 2):
                if times[i + 2] - times[i] < 60:
                    high.append(name)
                    break
        return high
