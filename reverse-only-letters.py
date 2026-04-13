class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s_list[i].isalpha():
                i += 1
                continue
            if not s_list[j].isalpha():
                j -= 1
                continue
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ''.join(s_list)
