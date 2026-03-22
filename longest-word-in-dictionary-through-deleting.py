class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def isSubsequence(sub: str, main: str) -> bool:
            i = 0
            j = 0
            while i < len(main) and j < len(sub):
                if main[i] == sub[j]:
                    j += 1
                i += 1
            return j == len(sub)

        longest_word = ""

        for word in dictionary:
            if isSubsequence(word, s):
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    if word < longest_word:
                        longest_word = word
        
        return longest_word
