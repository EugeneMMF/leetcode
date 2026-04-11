from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for entry in cpdomains:
            cnt_str, domain = entry.split()
            cnt = int(cnt_str)
            parts = domain.split('.')
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] = counts.get(sub, 0) + cnt
        return [f"{c} {d}" for d, c in counts.items()]
