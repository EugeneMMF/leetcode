class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * total_spaces
        spaces_between = total_spaces // (len(words) - 1)
        extra_spaces = total_spaces - spaces_between * (len(words) - 1)
        return (' ' * spaces_between).join(words) + ' ' * extra_spaces
