class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        goat_latin_words = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, word in enumerate(words):
            first_char = word[0]
            
            if first_char.lower() in vowels:
                modified_word = word + "ma"
            else:
                modified_word = word[1:] + first_char + "ma"
            
            modified_word += 'a' * (i + 1)
            
            goat_latin_words.append(modified_word)
        
        return ' '.join(goat_latin_words)
