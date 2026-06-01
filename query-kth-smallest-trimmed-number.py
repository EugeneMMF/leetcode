class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            trimmed.sort(key=lambda x: (x[0], x[1]))
            answer.append(trimmed[k-1][1])
        return answer
