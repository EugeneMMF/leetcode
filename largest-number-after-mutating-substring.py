class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        start = -1
        for i, ch in enumerate(num):
            d = int(ch)
            if change[d] > d:
                start = i
                break
        if start == -1:
            return num
        end = start
        while end < n:
            d = int(num[end])
            if change[d] < d:
                break
            end += 1
        mutated = list(num)
        for i in range(start, end):
            mutated[i] = str(change[int(num[i])])
        return ''.join(mutated)
