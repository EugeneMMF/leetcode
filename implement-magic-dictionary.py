class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for dict_word in self.dictionary:
            if len(dict_word) != n:
                continue

            diff_count = 0
            for i in range(n):
                if dict_word[i] != searchWord[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            
            if diff_count == 1:
                return True
        return False