class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = [(val, idx) for idx, val in enumerate(nums)]
        indexed.sort(key=lambda x: x[0], reverse=True)
        top_k = indexed[:k]
        top_k.sort(key=lambda x: x[1])
        return [val for val, _ in top_k]