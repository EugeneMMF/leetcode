class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        num_words = len(words)

        if num_words == 1:
            return words[0] + ' ' * spaces

        even_spaces = spaces // (num_words - 1)
        extra_spaces = spaces % (num_words - 1)

        result = (' ' * even_spaces).join(words)
        result += ' ' * extra_spaces

        return result

