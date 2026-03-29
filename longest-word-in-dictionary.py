class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        word_set = set()
        longest = ""

        for word in words:
            if len(word) == 1 or word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest

