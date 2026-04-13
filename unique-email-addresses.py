from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            plus_idx = local.find('+')
            if plus_idx != -1:
                local = local[:plus_idx]
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)
