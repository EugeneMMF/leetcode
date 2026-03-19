class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def can_break(s: str, word_set: set[str]) -> bool:
            n = len(s)
            if n == 0:
                return False

            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break

            return dp[n]

        word_set = set(words)
        
        result = []
        
        for current_word in words:
            word_set.remove(current_word)
            
            if can_break(current_word, word_set):
                result.append(current_word)
            
            word_set.add(current_word)
            
        return result
