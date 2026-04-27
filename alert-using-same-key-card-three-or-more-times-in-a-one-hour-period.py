class Solution:
    def alertNames(self, keyName, keyTime):
        from collections import defaultdict
        name_to_times = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            h, m = t.split(':')
            minutes = int(h) * 60 + int(m)
            name_to_times[n].append(minutes)
        alerted = []
        for name, times in name_to_times.items():
            if len(times) < 3:
                continue
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alerted.append(name)
                    break
        return sorted(alerted)
