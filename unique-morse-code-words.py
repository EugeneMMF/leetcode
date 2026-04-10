class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            transformed_word = ""
            for char in word:
                transformed_word += morse_code[ord(char) - ord('a')]
            transformations.add(transformed_word)
        return len(transformations)

