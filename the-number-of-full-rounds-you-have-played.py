class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        lh, lm = map(int, loginTime.split(':'))
        sh, sm = map(int, logoutTime.split(':'))
        login = lh * 60 + lm
        logout = sh * 60 + sm
        def count_between(start, end):
            if end <= start:
                return 0
            first = ((start + 14) // 15) * 15
            last = ((end - 15) // 15) * 15
            if last < first:
                return 0
            return (last - first) // 15 + 1
        if logout > login:
            return count_between(login, logout)
        else:
            return count_between(login, 1440) + count_between(0, logout)
