class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos = {}
        for x in nums:
            pos[x] = pos.get(x, 0) + 1
        for f, t in zip(moveFrom, moveTo):
            cnt = pos.pop(f)
            pos[t] = pos.get(t, 0) + cnt
        return sorted(pos.keys())