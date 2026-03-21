class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lower_word = word.lower()
            
            current_word_row = None
            
            if lower_word[0] in row1:
                current_word_row = row1
            elif lower_word[0] in row2:
                current_word_row = row2
            else:
                current_word_row = row3
            
            is_single_row_word = True
            for char in lower_word:
                if char not in current_word_row:
                    is_single_row_word = False
                    break
            
            if is_single_row_word:
                result.append(word)
                
        return result
