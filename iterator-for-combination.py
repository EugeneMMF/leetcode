class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.pointer = 0
        self._generate_combinations(characters, combinationLength, 0, [])

    def _generate_combinations(self, characters, k, start_index, current_combination):
        if len(current_combination) == k:
            self.combinations.append("".join(current_combination))
            return

        if len(current_combination) + (len(characters) - start_index) < k:
            return

        for i in range(start_index, len(characters)):
            current_combination.append(characters[i])
            self._generate_combinations(characters, k, i + 1, current_combination)
            current_combination.pop()

    def next(self) -> str:
        combination = self.combinations[self.pointer]
        self.pointer += 1
        return combination

    def hasNext(self) -> bool:
        return self.pointer < len(self.combinations)
