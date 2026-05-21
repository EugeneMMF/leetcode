class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s_list = list(s)
        i, j = 0, len(s_list) - 1
        moves = 0
        while i < j:
            k = j
            while k > i and s_list[k] != s_list[i]:
                k -= 1
            if k == i:
                s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
                moves += 1
            else:
                while k < j:
                    s_list[k], s_list[k + 1] = s_list[k + 1], s_list[k]
                    moves += 1
                    k += 1
                i += 1
                j -= 1
        return moves