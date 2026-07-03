class Solution:
    def findLatestTime(self, s: str) -> str:
        lst = list(s)
        if lst[0] == '?':
            if lst[1] == '?' or lst[1] <= '1':
                lst[0] = '1'
            else:
                lst[0] = '0'
        if lst[1] == '?':
            if lst[0] == '1':
                lst[1] = '1'
            else:
                lst[1] = '9'
        if lst[3] == '?':
            lst[3] = '5'
        if lst[4] == '?':
            lst[4] = '9'
        return "".join(lst)
