class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        lst = list(s)
        for i in range(n // 2):
            j = n - 1 - i
            if lst[i] != lst[j]:
                if lst[i] <= lst[j]:
                    lst[j] = lst[i]
                else:
                    lst[i] = lst[j]
        return ''.join(lst)
