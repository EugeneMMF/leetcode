class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {}
        for i, char in enumerate(order):
            order_map[char] = i

        def compare_words(word1, word2):
            len1, len2 = len(word1), len(word2)
            
            for i in range(max(len1, len2)):
                char1_rank = -1
                if i < len1:
                    char1_rank = order_map[word1[i]]
                
                char2_rank = -1
                if i < len2:
                    char2_rank = order_map[word2[i]]
                
                if char1_rank != char2_rank:
                    return char1_rank < char2_rank
            
            return True

        for i in range(len(words) - 1):
            if not compare_words(words[i], words[i+1]):
                return False
        
        return True
