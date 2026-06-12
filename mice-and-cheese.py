import typing
class Solution:
    def miceAndCheese(self, reward1: typing.List[int], reward2: typing.List[int], k: int) -> int:
        total = sum(reward2)
        diffs = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        diffs.sort(reverse=True)
        total += sum(diffs[:k])
        return total